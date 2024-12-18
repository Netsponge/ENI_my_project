
# from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse("Hello World! I'm Home.")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("My About page.")
    return render(request, 'about.html')
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Vue d'inscription (signup)
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "accounts/signup.html", {"form": form})

# Vue de connexion (login)
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')  # Rediriger vers la page d'accueil ou autre page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

# Vue de déconnexion (logout)
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("login")  # Redirige vers la page de login après déconnexion

