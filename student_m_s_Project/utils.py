import random
import string
from authAPP.models import Teacher, Student

def generate_registration_number():
    return 'REG' + ''.join(random.choices(string.digits, k=6))

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

def is_student(user):
    return Student.objects.filter(user=user).exists()

def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()

