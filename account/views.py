from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login # django packages for logging a user in
from .models import *
from django.contrib import messages

def home(request):
    context = {}
    return render(request, "account/index.html", context)

def register(request):
    if request.method == "POST":
        first_name = request.POST["fname"]
        last_name = request.POST["lname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirmpassword"]

        # create user if the passwords match and redirect home
        if password == confirm_password:
            user, created = User.objects.get_or_create(email=email, username = username, defaults={'first_name': first_name, 'last_name': last_name, 'password': password})
            login(request, user)
            return redirect('home')
        
        # throw and error message if a user tries to create an account with an existing mail in database
        messages.error(request, 'User with email already exists')
        return redirect('register')
    else:
        context = {}
        return render(request, "account/register.html", context)

def login_user(request):
    context = {}
    return render(request, "account/login.html", context)