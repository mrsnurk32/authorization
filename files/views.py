from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

#authentication modules
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

# Create your views here.

def login(request):
    pass


def register(request):
    pass


@login_required(login_url='accounts/login/')
def main(request):
    return render(request, 'files/main.html')