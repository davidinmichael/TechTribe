from django.shortcuts import render, redirect
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
            user = User.objects.create_user(email=email, username = username, defaults={'first_name': first_name, 'last_name': last_name, 'password': password})
            login(request, user)
            return redirect('login')
        else:
            # throw an error message if a user tries to create an account with an existing mail in database
            messages.error(request, 'User with email already exists')
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
            return redirect("register")
    
    else:
        context = {}
        return render(request, "account/login.html", context)
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect("home")