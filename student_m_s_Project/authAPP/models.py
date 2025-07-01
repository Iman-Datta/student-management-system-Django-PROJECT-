from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Link to built-in User model {One-to-One relationship}

    First_Name = models.CharField(max_length=100)
    Middle_Name = models.CharField(max_length=100, blank=True, null=True)
    Last_Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15)
    Father_Name = models.CharField(max_length=100)
    Mother_Name = models.CharField(max_length=100)
    gardian_phone_number = models.IntegerField()
    permanent_address = models.TextField()
    # Permanent_city = models.CharField(max_length=100)
    # permanent_state = models.CharField(max_length=100)
    # permanent_zip = models.IntegerField()
    current_address = models.TextField()
    # Current_city = models.CharField(max_length=100)
    # current_state = models.CharField(max_length=100)
    # current_zip = models.IntegerField()

    def save(self, *args, **kwargs ):
        return super().save(*args, **kwargs)

class Teacher(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Link to built-in User model

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    subject_specialization = models.CharField(max_length=100)
    # proof_document_upload = models.FileField(upload_to='proof_documents/', blank=True, null=True)   # File upload field for proof documents
    gender = models.CharField(max_length=10)