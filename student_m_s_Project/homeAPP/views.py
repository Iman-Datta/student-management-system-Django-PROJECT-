from django.http import HttpResponse
from django.shortcuts import render

def home(request: HttpResponse):
    context = {
        'title': 'Home Page',
        'message': 'Welcome to the Home Page!'
    }
    return render(request, 'index.html', context)