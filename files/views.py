#Visuals
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView

#messages
from django.contrib import messages

#authentication modules
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout


#Forms
from .forms import LoginForm

# Create your views here.


def login_view(request):


    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            return redirect('/')

        else:

            messages.error(request,'Неверный логин или пароль')
            return redirect('/accounts/login')

    else:

        form = LoginForm()

        context = {'form':form}

        return render(request,'files/login.html',context)


def register(request):
    pass


@login_required(login_url='accounts/login/')
def home(request):
    return render(request, 'files/wrapper.html')