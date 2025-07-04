from django.shortcuts import render,redirect
from django.http import HttpResponse
from authAPP.models import Student, Teacher
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib import messages
from utils import generate_registration_number, generate_password
from django.core.mail import send_mail



def registration(request: HttpResponse):
    context = {
        'title': 'Create Account',
        'message': 'Please fill in the form below to registrater.'
    }

    if request.method == 'POST':
        # Common input for all user
        fnm = request.POST.get('first_name')
        lnm = request.POST.get('last_name')
        user_email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if User.objects.filter(email=user_email).exists():
            return render(request, 'registration.html', {
                'error': True,
                'message': 'An account with this email already exists.'
            })
 
        if role == 'student':
            reg_number = generate_registration_number()
            user = User.objects.create_user(
                username=reg_number, # Username is set to registration number for students
                password=password,
                email=user_email,
                first_name=fnm,
                last_name=lnm
            )

            group = Group.objects.get(name='Student') # Call the student group from model
            user.groups.add(group) # Add the user to the group

            # Student-specific data
            bd = request.POST.get('dob')
            ph_num = request.POST.get('mobile')
            father_nm = request.POST.get('father_name')
            mother_mn = request.POST.get('mother_name')
            gardian_ph_num = int(request.POST.get('guardian_contact'))
            p_address = request.POST.get('permanent_address')
            p_city = request.POST.get('permanent_city')
            p_state = request.POST.get('permanent_state')
            p_zip = (request.POST.get('permanent_zip'))
            c_address = request.POST.get('current_address')
            c_city = request.POST.get('current_city')
            c_state = request.POST.get('current_state')
            c_zip = (request.POST.get('current_zip'))

            Student.objects.create(
                user=user,
                date_of_birth=bd,
                phone_number=ph_num,
                father_name=father_nm,
                mother_name=mother_mn,
                gardian_phone_number=gardian_ph_num,
                permanent_address=p_address,
                permanent_city=p_city,
                permanent_state=p_state,
                permanent_zip=p_zip,
                current_address=c_address,
                current_city=c_city,
                current_state=c_state,
                current_zip=c_zip)

            #  Send email before return
            send_mail(
                subject='Account Registration Confirmation',
                message=(
                    f'Dear {fnm},\n\n'
                    f'Your student account has been successfully created.\n'
                    f'Username (Reg No): {user.username}\n'
                    f'Password: {password}\n\n'
                    f'Please keep this information safe.\n\n'
                    f'Thank you!'
                ),
                from_email='dattaiman56@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
                )

            return render(request, 'homeAPP/index.html', {
                'success': True,
                'message': f'Student {fnm} added successfully',
                'reg_number': reg_number,
                'password': password
            })

        elif role == 'teacher':
            # Teacher-specific data
            department = request.POST.get('department')
            Subject_Specialization = request.POST.get('subject_specialization')
            mob_no = request.POST.get('mob')
            gender = request.POST.get('gender')

            user = User.objects.create_user(
                username=user_email,
                password=password,
                email=user_email,
                first_name=fnm,
                last_name=lnm
            )

            group = Group.objects.get(name='Teacher')
            user.groups.add(group)

            Teacher.objects.create(
                user=user,  
                department=department,
                subject_specialization=Subject_Specialization,
                mobile_number = mob_no,
                gender=gender,
            )

            send_mail(
                subject='Account Registration Confirmation',
                message=(
                    f'Dear {fnm},\n\n'
                    f'Your teacher account has been successfully created.\n'
                    f'Username: {user.username}\n'
                    f'Password: {password}\n\n'
                    f'Please keep this information safe.\n\n'
                    f'Thank you!'
                ),
                from_email='dattaiman56@gmail.com',
                recipient_list=[user_email],
                fail_silently=False,
                )
            return render(request, 'homeAPP/index.html', {
                'success': True,
                'message': f'Teacher {fnm} added successfully'
            })
    return render(request, 'registration.html', context)

def login_view(request: HttpResponse):
    if request.method == 'POST':
        reg_num = request.POST.get('reg_number')
        paswd = request.POST.get('password')
        
        user = authenticate(request, username=reg_num, password=paswd)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome {user.first_name}, you have successfully logged in!")
            return redirect ('_home')
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

def logout_view(request: HttpResponse):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('_home')