from django.urls import path, include
from . import views
from django.views.generic import TemplateView



urlpatterns = [
    path('' , views.main, name = 'main')
]
