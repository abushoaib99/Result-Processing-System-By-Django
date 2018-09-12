from django.contrib import admin
from .models import Informations, Marks, Semester
# Register your models here.

class Semester_Admin(admin.ModelAdmin):
    list_display = ['student_semester']

class Informations_Admin(admin.ModelAdmin):
    list_display = ['student_roll','student_department']

class Marks_Admin(admin.ModelAdmin):
    list_display = ['all_semester_student_semester','student_info_student_roll','student_info_student_department','subject_name',
                    'subject_marks','assignment_marks','midterm_marks','class_test_marks']

    def student_info_student_roll(self, instance):
        return instance.student_info.student_roll

    def student_info_student_department(self, instance):
        return instance.student_info.student_department

    def all_semester_student_semester(self, instance):
        return instance.all_semester.student_semester


admin.site.register(Informations,Informations_Admin)
admin.site.register(Marks,Marks_Admin)
admin.site.register(Semester,Semester_Admin)