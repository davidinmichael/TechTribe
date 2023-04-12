from django.shortcuts import render, redirect
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

        if password == confirm_password:
            user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
            )
            user.save()
            messages.success(request, "Welcome {username}, your account was successfully created.\nPlease Login")
            return redirect("login")
        else:
            return redirect("register")

    else:
        context = {}
        return render(request, "account/register.html", context)

def login(request):
    context = {}
    return render(request, "account/login.html", context)