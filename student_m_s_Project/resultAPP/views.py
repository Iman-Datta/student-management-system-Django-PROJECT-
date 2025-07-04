from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, render
from utils import is_student, is_teacher
from django.contrib import messages
from authAPP.models import Student, Teacher
from .models import Marksheet


@login_required
@permission_required('resultAPP.add_marksheet', raise_exception=True)
def result(request: HttpResponse):
    user = request.user
    if request.method == 'POST':
        # Handle form submission for adding a result
        try:
            teacher_profile = user.teacher
            subject = teacher_profile.subject_specialization.strip()
        except Teacher.DoesNotExist:
            messages.error(request, 'Teacher profile not found or subject not set.')
            return redirect('_home')

        reg_num = request.POST.get('reg_num')
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

        exam_date = request.POST.get('date')  # Add validation if needed

        Marksheet.objects.create(
            student=student,
            subject=subject,
            marks=marks,
            total_marks=total_marks,
            exam_date=exam_date
        )
        messages.success(request, f"Results added for student: {student.user.first_name}")
        return redirect('_result')  # Redirect after successful POST to avoid resubmission

    elif request.method == 'GET':
        if is_teacher(user):
            try:
                teacher_profile = user.teacher
                teacher_subject = teacher_profile.subject_specialization.strip()
                marksheets = Marksheet.objects.filter(subject__iexact=teacher_subject)
            except Teacher.DoesNotExist:
                messages.error(request, 'Teacher profile not found or subject not set.')
                return redirect('home')
            return render(request, 'resultAPP/result.html', {
                'title': 'Add Result',
                'marksheets': marksheets
            })
        else:
            messages.error(request, 'Access denied')
            return redirect('home')

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
