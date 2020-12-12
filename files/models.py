from django.db import models
from datetime import datetime as dt
# Create your models here.
class FileStorage(models.Model):


    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=120)
    created_date = models.DateTimeField(auto_now_add=True, blank = True)
    upload = models.FileField(upload_to = 'uploads/')