from django.db import models
from django.contrib import admin
from django.core.files.storage import FileSystemStorage


# Create your models here.
class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    contents=models.TextField()
    timestamp=models.DateTimeField()
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','contents','timestamp')
    
class UploadFile(models.Model):
    imgName=models.CharField(max_length=200)
    imgHead=models.FileField(upload_to='./mysite/static/upload')
    def __unicode__(self):
        return self.imgName
    
class RegistreUser(models.Model):
    uname=models.CharField(max_length=200)
    upwd=models.CharField(max_length=50)
    uemail=models.EmailField()

class UploadImage(models.Model):
    #fs = FileSystemStorage(location='/media/photos')
    img_name=models.CharField('image name',max_length=100)
    img_up=models.FileField(upload_to='./mysite/static/upload')
    def __unicode__(self):
        return self.img_name

