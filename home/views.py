from django.shortcuts import render, HttpResponse
from .models import Student
# Create your views here.
def home(request):

    return render(request, 'frontPage.html')
def student_info(request):
    all_student = Student.objects.all()
    context = {'all_student': all_student}
    return render(request, 'home/student_table.html', context)
