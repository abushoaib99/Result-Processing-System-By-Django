from django.contrib import admin
from .models import Student,Teacher
# Register your models here.
class Student_Admin(admin.ModelAdmin):
    list_display = ['student_name', 'student_id', 'session', 'semester']

class Teacher_Admin(admin.ModelAdmin):
    list_display = ['teacher_name', 'dept']


admin.site.register(Student, Student_Admin)
admin.site.register(Teacher, Teacher_Admin)
