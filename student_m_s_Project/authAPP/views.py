from django.shortcuts import render,redirect
from django.http import HttpResponse
from studentAPP.models import Student
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group
import random
import string

def generate_registration_number():
    return 'REG' + ''.join(random.choices(string.digits, k=6))

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def login_view(request: HttpResponse):
    if request.method == 'POST':
        reg_num = request.POST.get('reg_number')
        paswd = request.POST.get('password')
        user = authenticate(request, username=reg_num, password=paswd)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.first_name}, you have successfully logged in!")
            return redirect ('_after_login')
        else:
            messages.error(request,"Invalid registration number or password.")
            return redirect('_login')
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
        fnm=request.POST.get('first_name')
        mnm=request.POST.get('middle_name')
        lnm=request.POST.get('last_name')
        role = request.POST.get('role')
        bd=request.POST.get('dob')
        user_email=request.POST.get('email')
        if User.objects.filter(email=user_email).exists(): # filtering user by email
            return render(request, 'authapp/create_account.html',{
        'error': True,
        'message': 'An account with this email already exists.'
    })
        ph_num=request.POST.get('mobile')
        father_nm=request.POST.get('father_name')
        mother_mn=request.POST.get('mother_name')
        gardian_ph_num=int(request.POST.get('guardian_contact'))
        p_address=request.POST.get('permanent_address')
        p_city=request.POST.get('permanent_city')
        p_state=request.POST.get('permanent_state')
        p_zip=int(request.POST.get('permanent_zip'))
        c_address=request.POST.get('current_address')
        c_city=request.POST.get('current_city')
        c_state=request.POST.get('current_state')
        c_zip=int(request.POST.get('current_zip'))
        password = request.POST.get('password')
        reg_number = generate_registration_number()

        user = User.objects.create_user( # Create a new user for auth system
            username=reg_number,
            password=password,
            email = user_email,
            first_name=fnm,
            last_name=lnm
        )

        Student.objects.create( # Create a new student record in the Student model(coustom model created by me)
            user=user,
            First_Name=fnm,
            Middle_Name=mnm,
            Last_Name=lnm,
            Date_of_Birth=bd,
            Email=user_email,
            Phone_Number=ph_num,
            Father_Name=father_nm,
            Mother_Name=mother_mn,
            gardian_phone_number=gardian_ph_num,
            permanent_address=p_address,
            Permanent_city=p_city,
            permanent_state=p_state,
            permanent_zip=p_zip,
            current_address=c_address,
            Current_city=c_city,
            current_state=c_state,
            current_zip=c_zip
        )
        return render(request, 'authapp/create_account.html',{'success':True, 'message':'Student added successfully','reg_number': reg_number,
    'password': password})
    return render(request, 'authapp/create_account.html', context)

def logout_view(request: HttpResponse):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('_home')