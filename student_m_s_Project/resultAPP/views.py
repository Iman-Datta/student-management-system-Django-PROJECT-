from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from utils import is_student, is_teacher
from django.contrib import messages
from authAPP.models import Student, Teacher
from .models import Marksheet

@login_required
@permission_required('resultAPP.add_marksheet', raise_exception=True)
def teacher_result_view(request: HttpResponse):
    user = request.user

    # Handle POST: Add a new result
    if request.method == 'POST':
        if not is_teacher(user):
            return render(request, 'unauthorized.html', {'title': 'Unauthorized'})

        try:
            teacher_profile = user.teacher
            subject = teacher_profile.subject_specialization.strip()
        except Teacher.DoesNotExist:
            messages.error(request, 'Teacher profile not found or subject not set.')
            return redirect('_home')

        reg_num = request.POST.get('reg_num', '').strip()
        try:
            student = Student.objects.get(user__username=reg_num)
        except Student.DoesNotExist:
            messages.error(request, 'Invalid registration number.')
            return redirect('_result')

        try:
            total_marks = int(request.POST.get('total_marks'))
            marks = int(request.POST.get('marks'))
        except (ValueError, TypeError):
            messages.error(request, 'Marks and total marks must be integers.')
            return redirect('_result')

        exam_date = request.POST.get('date')  # Consider validating format

        # Create new marksheet entry
        Marksheet.objects.create(
            student=student,
            subject=subject,
            marks=marks,
            total_marks=total_marks,
            exam_date=exam_date
        )
        messages.success(request, f"Results added for student: {student.user.first_name}")
        return redirect('_result')

    # Handle GET: Search results or show all for this teacher
    elif request.method == 'GET':
        if not is_teacher(user):
            messages.error(request, 'Access denied.')
            return redirect('home')

        try:
            teacher_profile = user.teacher
            teacher_subject = teacher_profile.subject_specialization.strip()
        except Teacher.DoesNotExist:
            messages.error(request, 'Teacher profile not found or subject not set.')
            return redirect('home')

        # Filter by subject
        marksheets = Marksheet.objects.filter(subject__iexact=teacher_subject)

        # Optional filters from search form
        student_name = request.GET.get('student_name', '').strip()
        reg_num = request.GET.get('reg_num', '').strip()

        if student_name:
            marksheets = marksheets.filter(student__user__first_name__icontains=student_name)

        if reg_num:
            marksheets = marksheets.filter(student__user__username__icontains=reg_num)

        context = {
            'title': 'Result Page',
            'marksheets': marksheets,
        }
        return render(request, 'resultAPP/result.html', context)

    # Other request methods not allowed
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('home')

@login_required
def student_result_view(request: HttpResponse):
    user = request.user
    if is_student(user):
        try:
            student_profile = user.student
            marksheets = Marksheet.objects.filter(student=student_profile)
        except Student.DoesNotExist:
            messages.error(request, 'Student profile not found.')
            return redirect('home')

        return render(request, 'resultAPP/result.html', {
            'marksheets': marksheets,
            'title': 'Your Results'
        })
    else:
        messages.error(request, 'Access denied')
        return redirect('home')
    
@login_required
@permission_required('resultAPP.change_marksheet', raise_exception=True)
def edit_result_view(request, marksheet_id):
    user = request.user

    if not is_teacher(user):
        return render(request, 'unauthorized.html', {'title': 'Unauthorized'})
    try:
        marksheet = Marksheet.objects.get(id=marksheet_id)
    except Marksheet.DoesNotExist:
        messages.error(request, "Result not found.")
        return redirect('_result')

    if request.method == 'POST':
        try:
            marks = int(request.POST.get('marks'))
            total_marks = int(request.POST.get('total_marks'))
            exam_date = request.POST.get('date')  # Validate if necessary

            marksheet.marks = marks
            marksheet.total_marks = total_marks
            marksheet.exam_date = exam_date
            marksheet.save()

            messages.success(request, "Result updated successfully.")
            return redirect('_result')

        except (ValueError, TypeError):
            messages.error(request, 'Invalid data submitted.')

    context = {
        'marksheet': marksheet,
        'title': 'Edit Result',
    }
    return render(request, 'resultAPP/edit_result.html', context)