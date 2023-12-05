from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        # If the user is logged in, filter assignments for the logged-in user
        assignments = Assignment.objects.filter(uploaded_by=request.user)
    else:
        # Handle the case when the user is not logged in
        assignments = []

    return render(request, 'home.html', {'assignments': assignments})
    

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
  # Ensure the user is logged in to access this view
def submit(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')

        # Assuming you want to create a new assignment for the currently logged-in user
        assignment = Assignment(
            title=title,
            uploaded_by=request.user,
            file = request.FILES.get('file')
        )
        assignment.save()

        messages.success(request, 'Assignment submitted successfully!')
        return redirect('home')  # Redirect to a page showing a list of assignments

    return render(request, 'submit.html')  # Adjust the template name as needed

    