from django.shortcuts import render, redirect
from .models import Marks, Semester
from django.contrib.auth import authenticate, login as dj_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def login(request):

    if request.user.is_authenticated:
        return redirect('result:home')
    else:
        if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['pass']

            request.session['username'] = request.POST['user']
            request.session['password'] = request.POST['pass']

            try:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    if user.is_active:
                        dj_login(request, user)
                        return redirect('result:home')
                else:
                    messages.error(request, 'Username and Password not match')
            except ObjectDoesNotExist:
                print("invalid User")
        return render(request, 'login.html')


@login_required(login_url='result:login')
def home(request):
    password = request.session['password']
    context = {
        'semester': Semester.objects.all(),
        'dept': request.session['username'],
        'roll': password[4:8]
    }
    if request.method == 'POST':
        selected_semester = 0
        selected_semester = request.POST['semester']
        if selected_semester != 0:
            return redirect('result:marks', selected_semester)

    return render(request, 'FrontPage.html', context)



@login_required(login_url='result:login')
def marks_table(request, selected_semester):
    print(selected_semester,type(selected_semester))
    dept = request.session['username']
    roll = request.session['password']
    roll = roll[4:8]

    all_marks = Marks.objects.filter(all_semester__id=selected_semester).filter(student_info__student_roll=roll).filter(student_info__student_department=dept)

    if len(all_marks)!=0:
        total = []
        point = []
        for i in range(0, len(all_marks)):
            t = all_marks[i].subject_marks + all_marks[i].assignment_marks + all_marks[i].class_test_marks + all_marks[i].midterm_marks
            total.append(t)
            if t >= 80:
                point.append(4.00)
            elif t<80 and t >= 75:
                point.append(3.75)
            elif t < 75 and t >= 70:
                point.append(3.50)
            elif t < 70 and t >= 65:
                point.append(3.25)
            elif t < 65 and t >= 60:
                point.append(3.00)
            elif t < 60 and t >= 55:
                point.append(2.75)
            elif t < 55 and t >= 50:
                point.append(2.50)
            elif t < 50 and t >= 45:
                point.append(2.25)
            elif t < 45 and t >= 40:
                point.append(2.00)
            else:
                point.append(0.00)

        if selected_semester == 1:
            gpa = sum(point)*3/16.5
        elif selected_semester == 2:
            gpa = sum(point)*3/18
        elif selected_semester == 3:
            gpa = sum(point)*3/22.5
        elif selected_semester == 4:
            gpa = sum(point)*3/18.0
        elif selected_semester == 5:
            gpa = sum(point)*3/16.5
        elif selected_semester == 6:
            gpa = sum(point)*3/19.5
        elif selected_semester == 7:
            gpa = sum(point)*3/17.5
        elif selected_semester == 8:
            gpa = sum(point) * 3 / 16.5

        gpa = format(gpa, '.2')
        context = {
            'all_student': list(zip(total, point, all_marks)),
            'gpa': gpa
        }
        return render(request, 'student_table.html', context)

    else:
        context = {
            'all_student': all_marks
        }
        return render(request, 'student_table.html', context)



def log(request):
    logout(request)
    return redirect('result:login')