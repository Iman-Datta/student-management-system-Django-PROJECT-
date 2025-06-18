from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request: HttpResponse):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home Page!'
    }
    return render(request, 'index.html', context)

def result(request: HttpResponse):
    context = {
        'title': 'Result Page',
        'message': 'This is the Result Page!'
    }
    return render(request, 'result.html', context)

def payment(request: HttpResponse):
    context = {
        'title': 'Payment Page',
        'message': 'This is the Payment Page!'
    }
    return render(request, 'payment.html', context)

def registration(request: HttpResponse):
    context = {
        'title': 'Registration Page',
        'message': 'This is the Registration Page!'
    }
    return render(request, 'registration.html', context)