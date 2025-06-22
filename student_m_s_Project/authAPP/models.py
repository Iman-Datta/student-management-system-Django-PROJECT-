from django.db import models

class Student(models.Model):
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