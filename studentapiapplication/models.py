from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=500)
    student_age = models.IntegerField()
    student_school = models.CharField(max_length=1000)

    def __str__(self):
        return self.student_name