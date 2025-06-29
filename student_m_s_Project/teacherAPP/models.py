from django.db import models

class Teacher(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)  # Link to built-in User model

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    subject_specialization = models.CharField(max_length=100)
    proof_document_upload = models.FileField(upload_to='proof_documents/', blank=True, null=True)   # File upload field for proof documents
    gender = models.CharField(max_length=10)