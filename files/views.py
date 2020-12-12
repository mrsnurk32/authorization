#Visuals
from django.shortcuts import render, redirect
from django.views.generic import View
from django.views.generic import TemplateView
from django.core.paginator import Paginator


#messages
from django.contrib import messages

#authentication modules
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

#Reg form
from django.contrib.auth.forms import UserCreationForm


#Forms
from .forms import LoginForm

#Models
from .models import FileStorage


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


    if request.method == 'POST':
    
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
    
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    
        return redirect('/')
    
    else:
    
        form = UserCreationForm()
    
    return render(request, 'files/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('accounts/login/')


@login_required(login_url='accounts/login/')
def home(request):
    user_data = request.user

    file_list = FileStorage.objects.all()
    paginator = Paginator(file_list, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'user_data':user_data,
        'page_obj':page_obj
    }
    return render(request, 'files/file_list.html', context)