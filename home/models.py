from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Semester(models.Model):
    sem = (
        ('1st Semester', '1st Semester'),
        ('2nd Semester', '2nd Semester'),
        ('3rd Semester', '3rd Semester'),
        ('4th Semester', '4th Semester'),
        ('5th Semester', '5th Semester'),
        ('6th Semester', '6th Semester'),
        ('7th Semester', '7th Semester'),
        ('8th Semester', '8th Semester')
    )

    student_semester = models.CharField(max_length=15, choices=sem,unique=True)

    def __str__(self):
        return self.student_semester


class Informations(models.Model):
    department = (
        ('CSE', 'CSE'),
        ('ECE', 'ECE'),
        ('BBA', 'BBA')
    )

    student_roll = models.PositiveIntegerField(default=0)
    student_department = models.CharField(max_length=4, choices=department)

    class Meta:
        unique_together = (('student_roll', 'student_department'),)

    def __str__(self):
        return self.student_department+', '+self.student_roll.__str__()


class Marks(models.Model):
    student_info = models.ForeignKey(Informations, on_delete=models.CASCADE)
    all_semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    subject_marks = models.PositiveIntegerField(default=0,validators=[MaxValueValidator(100)])
    assignment_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])
    midterm_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10)])
    class_test_marks = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])

    class Meta(object):
        unique_together = (('student_info','subject_name'),)
        ordering = ['all_semester']

    def __str__(self):
        return self.subject_name+', '+self.subject_marks.__str__()+', '+self.assignment_marks.__str__()+', '+self.midterm_marks.__str__()+', '+self.class_test_marks.__str__()+', '+self.student_info.student_roll.__str__()+', '+self.all_semester.student_semester+', '+self.student_info.student_department





