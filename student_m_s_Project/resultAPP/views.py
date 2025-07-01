from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from resultAPP.models import Marksheet
from utils import is_student, is_teacher
from authAPP.models import Student

@login_required
def add_result(request: HttpResponse):
    if request.method == 'POST':
        if is_student(user= request.user):
            messages.error(request, 'Access denied')
            return redirect('home.html')
        elif is_teacher(user= request.user):
            reg_num = request.POST.get('reg_num')
            exam_date = request.POST.get('date')
            total_marks = request.POST.get('total_marks')
            marks = request.POST.get('marks')
            # Get teacher's subject from their profile
            try:
                teacher = request.user.teacher
                subject = teacher.subject_specialization.strip()
            except:
                messages.error(request, "Teacher profile not found or subject not set.")
                return redirect('_add_result')
            try:
                student = Student.objects.get(user__username=reg_num)
            except Student.DoesNotExist:
                messages.error(request, 'Invalid registration number.')
                return redirect('_add_result')
            
            Marksheet.objects.create(
                student=student,
                subject=subject,
                marks=int(marks),
                total_marks=int(total_marks),
                exam_date=exam_date
            )

            messages.success(request, f"Results added for student: {student.First_Name}")
            return redirect('_view_result')
    return render(request, 'result.html')

@login_required
def view_result(request: HttpResponse):
    if is_teacher(user=request.user):
        marksheets = Marksheet.objects.all()
        context = {
            'title': 'Result Page',
            'marksheets': marksheets
        }
        return render(request, 'result.html', context)
    
    elif is_student(user=request.user):
        student = request.user.student
        if not student:
            messages.error(request, 'You are not registered as a student.')
            return redirect('_login')
        else:
            marksheets = Marksheet.objects.filter(student=student)
            fnm = request.user.first_name
            lnm = request.user.last_name
            reg_number = request.user.username
            context = {
                'title': 'Result Page',
                'name': f'{fnm} {lnm}',
                'reg_number': reg_number,
                'marksheets': marksheets
            }
            return render(request, 'result.html', context)
    else:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('_login')
    
@login_required
def update_result(request: HttpResponse):
    if is_student(user = request.user):
        messages.error(request, 'Access denied')
        return redirect('home.html')
    elif is_teacher(user = request.user):
        teacher =  request.user.teacher
        subject = teacher.subject_specialization.strip()
        reg_num = request.POST.get('reg_num')
        try:
            student = Student.objects.get(user__username=reg_num)
        except Student.DoesNotExist:
            messages.error(request, 'Invalid registration number.')
            return redirect('_add_result')
        exam_date = request.POST.get('date')
        new_marks = request.POST.get('marks')
        total_marks = request.POST.get('total_marks')

        if not new_marks or not total_marks or not new_marks.isdigit() or not total_marks.isdigit():
            messages.error(request, "Invalid marks or total marks.")
            return redirect('_add_result')

        # Fetch the specific Marksheet entry
        try:
            marksheet = Marksheet.objects.get(student=student, subject=subject, exam_date=exam_date)
        except Marksheet.DoesNotExist:
            messages.error(request, f"No result found for {subject} on {exam_date}")
            return redirect('_add_result')

        # Update the result
        marksheet.marks = int(new_marks)
        marksheet.total_marks = int(total_marks)
        marksheet.save()

        messages.success(request, f"{subject} marks updated for student {student.First_Name}")
        return redirect('_view_result')