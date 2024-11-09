from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'app/login.html')


@login_required
def home_view(request):
    student = Student.objects.filter(teacher=request.user)
    return render(request, 'app/home.html', {'student': student})


@login_required
def add_student_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        marks = int(request.POST['marks'])

        student, created = Student.objects.get_or_create(
            name=name,
            subject=subject,
            teacher=request.user,
            defaults={'marks': marks}
        )

        if not created:
            student.marks += marks
            student.save()

        return redirect('home')
    return render(request, 'app/home.html')


@login_required
def edit_student_view(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return redirect(request, 'app/home.html', context)


def update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        marks = request.POST.get('marks')

        student = Student(
            id=id,
            name=name,
            subject=subject,
            marks=marks,
            teacher=request.user,

        )
        student.save()
        return redirect('home')


    return redirect(request, 'app/home.html')


@login_required
def delete_student_view(request, id):
    student = Student.objects.filter(id=id, teacher=request.user)
    student.delete()
    context = {
        'student': student,
    }
    return redirect('home')






@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

