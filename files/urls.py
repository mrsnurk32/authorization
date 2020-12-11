from django.urls import path, include
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('' , views.home, name = 'main'),
    path('accounts/login/', views.login_view, name = 'login_form')
]
