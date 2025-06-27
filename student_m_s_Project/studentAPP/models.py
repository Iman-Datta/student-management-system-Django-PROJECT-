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
    Permanent_city = models.CharField(max_length=100)
    permanent_state = models.CharField(max_length=100)
    permanent_zip = models.IntegerField()
    current_address = models.TextField()
    Current_city = models.CharField(max_length=100)
    current_state = models.CharField(max_length=100)
    current_zip = models.IntegerField()

    def save(self, *args, **kwargs ):
        return super().save(*args, **kwargs)

class Marksheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # many to one relationship with Student
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    exam_date = models.DateField()
    grade = models.CharField(max_length=2)

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)