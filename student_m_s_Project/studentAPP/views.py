from django.shortcuts import render,redirect
from django.http import HttpResponse

def result(request: HttpResponse):
    context = {
        'title': 'Result Page',
        'message': 'This is the Result Page!'
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