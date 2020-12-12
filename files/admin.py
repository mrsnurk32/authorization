from django.contrib import admin
from .models import FileStorage
# Register your models here.

@admin.register(FileStorage)
class AdminFiles(admin.ModelAdmin):
    model = FileStorage
    list_display = ('file_name','upload')

