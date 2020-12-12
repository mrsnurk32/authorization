from django.db import models

# Create your models here.
class FileStorage(models.Model):

    file_name = models.CharField(max_length=120)
    upload = models.FileField(upload_to = 'uploads/')