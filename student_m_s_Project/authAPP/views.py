from django.shortcuts import render,redirect
from django.http import HttpResponse
from authAPP.models import Student

def login(request: HttpResponse):

    if request.method == 'POST':
        reg_num = request.POST.get('reg_num')
        paswd = request.POST.get('paswd')
        return render(request, 'authapp/login/login.html')
    return render(request, 'authapp/login/login.html')

def forgot_password(request: HttpResponse):
    if request.method == 'POST':
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        
        # Here you would typically handle the password reset logic
        # For now, we just print the values to the console
        print(f"Date of Birth: {dob}")
        print(f"Email: {email}")
        return render(request, 'authapp/login/forgot_password.html', {'message': 'Password reset instructions sent.'})
    return render(request, 'authapp/login/forgot_password.html')

def create_account(request: HttpResponse):
    context = {
    'title': 'Create Account',
    'message': 'Please fill in the form below to create your account.'
    }
    if request.method == 'POST':
        response = Student.objects.create(
            First_Name=request.POST.get('first_name'),
            Middle_Name=request.POST.get('middle_name'),
            Last_Name=request.POST.get('last_name'),
            Date_of_Birth=request.POST.get('dob'),
            Email=request.POST.get('email'),
            Phone_Number=request.POST.get('mobile'),
            Father_Name=request.POST.get('father_name'),
            Mother_Name=request.POST.get('mother_name'),
            gardian_phone_number=int(request.POST.get('guardian_contact')),
            permanent_address=request.POST.get('permanent_address'),
            Permanent_city=request.POST.get('permanent_city'),
            permanent_state=request.POST.get('permanent_state'),
            permanent_zip=int(request.POST.get('permanent_zip')),
            current_address=request.POST.get('current_address'),
            Current_city=request.POST.get('current_city'),
            current_state=request.POST.get('current_state'),
            current_zip=int(request.POST.get('current_zip'))
        )
        # response.save()
        return render(request, 'authapp/create_account.html',{'success':True, 'message':'Student added successfully'})
    return render(request, 'authapp/create_account.html', context)

def logout(request: HttpResponse):
    context = {
        'title': 'Logout Page',
        'message': 'You have been logged out!'
    }
    return render(request, 'authapp/logout.html', context)