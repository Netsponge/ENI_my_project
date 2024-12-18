# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Formulaire d'inscription (Signup)
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulaire de connexion (Login)
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully.")
            login(request, user)  # Connecte l'utilisateur après la création du compte
            return redirect('home')  # Redirige vers la page d'accueil après inscription
        else:
            messages.error(request, "There was an error with the registration form.")
    else:
        form = SignUpForm()
        

    return render(request, "accounts/signup.html", {"form": form})
