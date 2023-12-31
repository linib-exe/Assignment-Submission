from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    stu = None
    if request.user.is_authenticated:
        # If the user is logged in, filter assignments for the logged-in user
        assignments = Assignment.objects.filter(uploaded_by=request.user)
        stu = Student.objects.get(user=request.user)
        
    else:
        # Handle the case when the user is not logged in
        assignments = []

    return render(request, 'home.html', {'assignments': assignments,'student':stu})
    

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        faculty = request.POST.get('faculty')
        rollno = request.POST.get('rollno')
        semester = request.POST.get('semester')
        section = request.POST.get('section')
        passkey = request.POST.get('password')

        # Assuming you want to create a new user with the student's name as the username
        user = User.objects.create_user(username=contact, 
                                        password=passkey)  # Set a default password

        # Create a new student instance
        student_instance = Student(user=user, 
                                   name=name, 
                                   faculty=faculty, 
                                   rollno=rollno, 
                                   semester=semester, 
                                   section=section,
                                   contact=contact,
                                   password=passkey)
        student_instance.save()
        login(request,user)
        return redirect('home')  # Redirect to a success page or wherever you want

    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,
                                    password=password)
        if user is not None:
            login(request,user)
            print("Login Successful")
            return redirect('home')
        else:
            error_message = "Invalid Login"
            print(error_message)
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def teacher_dashboard(request):
    stu = None
    if request.user.is_authenticated and request.user.student.isteacher:
        stu = Student.objects.get(user=request.user)
        assignments = Assignment.objects.all()
        return render(request, 'dashboard.html', {'assignments': assignments,'student':stu})
    return render(request,'dashboard.html',{'student':stu})


@login_required(login_url='login')
def submit(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        file = request.FILES.get('file')
        
        assignment = Assignment(
            title=title,
            uploaded_by=request.user,
            file = file
        )
        assignment.save()

        messages.success(request, 'Assignment submitted successfully!')
        return redirect('home')  
    return render(request, 'submit.html',{'student':student})  

@login_required(login_url='login')
def update_assignment(request,id):
    assignment = None
    if request.user.is_authenticated and request.user.student.isteacher:
        assignment = Assignment.objects.get(pk=id)
        if request.method == 'POST':
            status = request.POST.get('status')
            remarks = request.POST.get('remarks')

            assignment.status = status
            assignment.remarks = remarks
            assignment.save()

            messages.success(request, 'Assignment updated successfully!')
            return redirect('dashboard') 
    return render(request,'update_assignment.html',{'assignment':assignment})


    