from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout # django packages for logging a user in
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import *
from django.urls import reverse


def home(request):
    context = {
        "title" : "Home"
    }
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

            # Create a profile instance and associate it with the User instance
            profile = Profile.objects.create(user=user, full_name=f"{first_name} {last_name}")
            profile.save()
            messages.success(request, f"{username}, your account has been created successfully")
            return redirect('login')
        
        # throw an error message if the passwords do not match
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        context = {
            "title" : "Register"
        }
        return render(request, "account/register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{username}, Login succesfull")
            return redirect(reverse("profile", args=[user.username]))
        else:
            messages.error(request, "Invalid Credentials, Please, try again.")
            return redirect("login")
    
    else:
        context = {
            "title" : "Login"
        }
        return render(request, "account/login.html", context)
    
def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect("login")

@login_required
def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
        "profile" : profile
    }
    return render(request, "account/profile.html", context)

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect(reverse("profile", args=[user.username]))
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'account/editprofile.html', context)
