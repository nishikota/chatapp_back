from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, LoginForm

# Create your views here.
