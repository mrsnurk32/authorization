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

#rest api
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.

class FileUpload(APIView):
    parser_class = (FileUploadParser,)

    def put(self, request, format=None):

        if 'file' not in request.data:
            raise ParseError("Empty content")
        print(request.data)
        f = request.data['file']

        FileStorage.objects.create(
            file_name = request.data['file_name'],
            upload = request.data['file']
        )
        # mymodel.my_file_field.save(f.name, f, save=True)

        return Response(status=status.HTTP_201_CREATED)


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
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def view_file(request, file_id):

    file = FileStorage.objects.get(file_id = file_id)
    file = open('media/' + str(file.upload),'r').read()
    rows = file.split('\n')

    final_list = [row.split(',') for row in rows]

    user_data = request.user
    context = {
        'user_data':user_data,
        'file_data':final_list
    }


    return render(request, 'files/view_file.html',context)