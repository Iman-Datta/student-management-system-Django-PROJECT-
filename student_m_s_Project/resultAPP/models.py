from django.db import models
from authAPP.models import Student


class Marksheet(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE) # many to one relationship with Student
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    total_marks = models.IntegerField(default=0)  # Total marks for the subject
    exam_date = models.DateField()
    percentage = models.FloatField(default=0.0)  # Percentage of marks obtained
    grade = models.CharField(max_length=2)

    def calculate_grade(self):
        if self.percentage >= 90:
            return 'A+'
        elif self.percentage >= 80:
            return 'A'
        elif self.percentage >= 70:
            return 'B+'
        elif self.percentage >= 60:
            return 'B'
        elif self.percentage >= 50:
            return 'C'
        elif self.percentage >= 40:
            return 'D'
        else:
            return 'F'

    def calculate_percentage(self):
        percentage = (self.marks / self.total_marks) * 100
        return percentage

    def save(self, *args, **kwargs):
        self.percentage = self.calculate_percentage()
        self.grade = self.calculate_grade()
        return super().save(*args, **kwargs)