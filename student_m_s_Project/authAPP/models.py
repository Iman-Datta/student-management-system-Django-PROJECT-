from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Link to built-in User model {One-to-One relationship}

    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=15) # For +91 ****
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    gardian_phone_number = models.IntegerField()
    permanent_address = models.TextField()
    permanent_city = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=100)
    permanent_zip = models.CharField(max_length=10)
    current_address = models.TextField()
    current_city = models.CharField(max_length=100)
    current_state = models.CharField(max_length=100)
    current_zip = models.CharField(max_length=10)

    def save(self, *args, **kwargs ):
        return super().save(*args, **kwargs)

class Teacher(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Link to built-in User model

    department = models.CharField(max_length=100)
    subject_specialization = models.CharField(max_length=100)
    mobile_number  = models.CharField(max_length=10)
    # proof_document_upload = models.FileField(upload_to='proof_documents/', blank=True, null=True)   # File upload field for proof documents
    gender = models.CharField(max_length=10)