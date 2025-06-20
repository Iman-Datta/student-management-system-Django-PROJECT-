from django.shortcuts import render,redirect
from django.http import HttpResponse

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
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        paswd = request.post.get('paswd')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        guardian_contact = request.POST.get('guardian_contact')
        permanent_address = request.POST.get('permanent_address')
        permanent_city  = request.POST.get('permanent_city')
        permanent_state = request.POST.get('permanent_state')
        permanent_zip = request.POST.get('permanent_zip')
        current_address = request.POST.get('current_address')
        current_city = request.POST.get('current_city')
        current_state = request.POST.get('current_state')
        current_zip = request.POST.get('current_zip')

# Just checking if the form is submitted
        print(f"First Name: {first_name}")
        print(f"Middle Name: {middle_name}")
        print(f"Last Name: {last_name}")
        print(f"Email: {email}")
        print(f"Mobile: {mobile}")
        print(f"Father's Name: {father_name}")
        print(f"Mother's Name: {mother_name}")
        print(f"Guardian Contact: {guardian_contact}")
        print(f"Permanent Address: {permanent_address}, {permanent_city}, {permanent_state}, {permanent_zip}")
        print(f"Current Address: {current_address}, {current_city}, {current_state}, {current_zip}")

        return render(request, 'authapp/create_account.html', context)
    return render(request, 'authapp/create_account.html', context)

def logout(request: HttpResponse):
    context = {
        'title': 'Logout Page',
        'message': 'You have been logged out!'
    }
    return render(request, 'authapp/logout.html', context)