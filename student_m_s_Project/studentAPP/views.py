
from django.shortcuts import render,redirect
from django.http import HttpResponse

def payment(request: HttpResponse):
    context = {
        'title': 'Payment Page',
        'message': 'This is the Payment Page!'
    }
    return render(request, 'studentAPP/payment.html', context)
