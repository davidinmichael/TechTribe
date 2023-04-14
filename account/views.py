from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout # django packages for logging a user in
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
            # check if the user already exists in the database
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User with email already exists')
                return redirect('register')

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            # login(request, user)
            return redirect('login')
        
        # throw an error message if the passwords do not match
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        context = {}
        return render(request, "account/register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login succesfull")
            return redirect("home")
        else:
            messages.error(request, "Invalid Credentials, Please, try again.")
            return redirect("login")
    
    else:
        context = {}
        return render(request, "account/login.html", context)
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect("home")