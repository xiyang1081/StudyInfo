#!/usr/bin/env python
#code=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from blog.models import BlogPost,UploadFile,RegistreUser
from django.template import loader,Context
from django import forms

# Create your views here.
def archive(request):
    posts=BlogPost.objects.all()
    for pos in posts:
        print pos.title
    #print posts.all()
    t=loader.get_template('blog/archive.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))
def blogShow(request):
    listTitle=request.GET.get('title')
    posts=BlogPost.objects.get(title=listTitle)
    print 'title',posts.title,posts.timestamp
    t=loader.get_template('blog/blogshow.html')
    c=Context({'posts':posts})
    return HttpResponse(t.render(c))

class FileForm(forms.Form):
    filename=forms.CharField()
    filehead=forms.FileField()
    
def register(request):
    if request.method=='POST':
        uf=FileForm(request.POST,request.FILES)
        if uf.is_valid():
            filename=uf.cleaned_data['filename']
            filehead=uf.cleaned_data['filehead']
            
            fileup=UploadFile()
            fileup.imgName=filename
            fileup.imgHead=filehead
            fileup.save()            
            return HttpResponse('Upload OK!')
        else:
            return render_to_response('blog/register.html')
    else:
        uf=FileForm()
            
    return render_to_response('blog/register.html',{'uf':uf})

#Register User
class UserForm(forms.Form):
    username=forms.CharField(label='User:',max_length=200)
    password=forms.CharField(label='Password:',widget=forms.PasswordInput())
    email=forms.EmailField(label='Email:')
    
def registerUser(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            email=uf.cleaned_data['email']
            
            user=RegistreUser()
            user.uname=username
            user.upwd=password
            user.uemail=email
            user.save()
            return render_to_response('blog/success.html',{'username':username})
    else:
        uf=UserForm()
    return render_to_response('blog/registerUser.html',{'uf':uf})