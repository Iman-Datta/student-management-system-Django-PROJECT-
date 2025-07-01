import random
import string

def generate_registration_number():
    return 'REG' + ''.join(random.choices(string.digits, k=6))

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def is_student(user):
    return user.groups.filter(name='Student').exists()

def is_teacher(user):
    return user.groups.filter(name='Teacher').exists()
