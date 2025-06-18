from django.shortcuts import render,redirect
from django.http import HttpResponse

def login(request: HttpResponse):
    context = {
        'title': 'Login Page',
        'message': 'This is the Login Page!'
    }
    return render(request, 'login.html', context)
def create_account(request: HttpResponse):
    context = {
        'title': 'Create Account Page',
        'message': 'This is the Create Account Page!'
    }
    return render(request, 'create_account.html', context)
def logout(request: HttpResponse):
    context = {
        'title': 'Logout Page',
        'message': 'You have been logged out!'
    }
    return render(request, 'logout.html', context)