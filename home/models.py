from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    student_id = models.IntegerField(default=0)
    dept = models.CharField(max_length=100)
    session = models.DateField(default=0)
    semester = models.CharField(max_length=500)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
