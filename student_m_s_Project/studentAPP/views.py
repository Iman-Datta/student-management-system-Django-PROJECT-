
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Student, Marksheet

@login_required
def result(request: HttpResponse):
    student = request.user.student
    if not student:
        messages.error(request, 'You are not registered as a student.')
        return redirect('_login')
    else:
        fnm = request.user.first_name
        lnm = request.user.last_name
        reg_number = request.user.username  # this is your REGxxxx
        marksheets = Marksheet.objects.filter(student=student)

        context = {
            'title': 'Result Page',
            'name': f'{fnm} {lnm}',
            'reg_number': reg_number,
            'marksheets': marksheets
        }
    return render(request, 'studentAPP/result.html', context)

def payment(request: HttpResponse):
    context = {
        'title': 'Payment Page',
        'message': 'This is the Payment Page!'
    }
    return render(request, 'studentAPP/payment.html', context)

def registration(request: HttpResponse):
    context = {
        'title': 'Registration Page',
        'message': 'This is the Registration Page!'
    }
    return render(request, 'studentAPP/registration.html', context)