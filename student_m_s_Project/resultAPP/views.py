from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render
from utils import is_student, is_teacher
from django.contrib import messages
from authAPP.models import Student, Teacher
from .models import Marksheet

@login_required
def add_result(request: HttpResponse):
    marksheets = Marksheet.objects.all()
    if request.method == 'POST':
        user = request.user
        if is_student(user):
            messages.error(request, 'Access denied')
            return redirect ('home')
        if is_teacher(user):
            try:
                teacher_profile = Teacher.objects.get(user=request.user) # teacher = request.user.teacher                
                subject = teacher_profile.subject_specialization.strip()
            except:
                messages.error(request, 'Teacher profile not found or subject not set.')
                return redirect('home')
            reg_num = request.POST.get('reg_num')
            print("Submitted reg number:", reg_num)
            try:
                # for s in Student.objects.all():
                    # print("Existing student username:", s.user.username)
                student = Student.objects.get(user__username=reg_num)
                # print(student)
            except Student.DoesNotExist:
                messages.error(request, 'Invalid registration number.')
                return redirect('_add_result')
            total_marks = request.POST.get('total_marks')
            marks = request.POST.get('marks')
            exam_date = request.POST.get('date')

            Marksheet.objects.create(
                student=student,
                subject=subject,
                marks=int(marks),
                total_marks=int(total_marks),
                exam_date=exam_date
            )

            messages.success(request, f"Results added for student: {student.user.first_name}")
            return redirect('_view_result')
    else:
        return render(request, 'add_result.html', {'marksheets': marksheets, 'title': 'Add Result'})
    
@login_required
def view_result(request: HttpResponse):
    if request.method == 'GET':
        user = request.user
        if is_student(user):
            try:
                student_profile = request.user.student
            except Student.DoesNotExist:
                messages.error(request, 'Student profile not found or subject not set.')
                return redirect('home')
            marksheet = Marksheet.objects.filter(student=student_profile)
            return render(request, 'view_result.html', {'marksheet': marksheet})
        elif is_teacher(user):
            try:
                teacher_profile = request.user.teacher
                teacher_subject = teacher_profile.subject_specialization.strip()
            except Teacher.DoesNotExist:
                messages.error(request, 'Teacher profile not found or subject not set.')
                return redirect('home')
            marksheet = Marksheet.objects.filter(subject__iexact = teacher_subject) # Case-insensitive filter
            return render(request, 'view_result.html', {'marksheet': marksheet})
        else:
            messages.error(request, 'Access denied')
            return redirect('home')
    return render (request, 'view_result.html')