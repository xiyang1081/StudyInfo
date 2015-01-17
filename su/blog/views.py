#!/usr/bin/env python
#coding=utf-8
from django.shortcuts import render,HttpResponse,render_to_response
from blog.models import SecondMenu,FirstMenu,BlogContent,BlogAnswer
from django import forms
from  DjangoUeditor.widgets import UEditorWidget
from  DjangoUeditor.forms import UEditorField, UEditorModelForm
from blog import models
#from django.utils import simplejson
import json
from django.core import serializers

# Create your views here.

class QuerySetEncoder(json.JSONEncoder):
    """
    Encoding QuerySet into JSON format
    """
    def default(self,object):
        try:
            return serializers.serialize("python",object,ensure_ascii=False)
        except:
            return json.JSONEncoder.default(self.object)


def home(request):
    first_menu=FirstMenu.objects.order_by('id')
    #print first_menu
    return render_to_response('blog/index.html',{'menu':first_menu})

#@csrf_exempt
def secondShow(request):
    """"
    显示二级导航栏
    """
    if request.method == "POST" and request.POST.has_key('second_id'):
        show_id=request.POST['second_id']        
    else:
        show_id=5
    #print 'show_id:',show_id
    second_menu=SecondMenu.objects.filter(parent_menu=show_id).order_by()
    #second_menu=SecondMenu.objects.order_by('id')
    #print second_menu
    second_items=[]
    for se in second_menu:
        #print se
        second_items.append({"second_items":se.second_menu,"second_id":se.id})
    #print second_items
    return HttpResponse(json.dumps(second_items,cls=QuerySetEncoder))
def listContent(request):
    if request.method == "POST" and request.POST.has_key('parent_id'):
        show_id=request.POST['parent_id']
    else:
        show_id=5
    blogList=BlogContent.objects.filter(bc_Style=show_id)
    blog_items=[]
    for bc in blogList:
        print bc.bc_Name,bc.bc_Datetime,bc.bc_Description
        bc_time=str(bc.bc_Datetime)[:19]
        blog_items.append({'bc_name':bc.bc_Name,'bc_id':bc.id,"bc_time":bc_time,"bc_Mark":bc.bc_Mark,"bc_id":bc.id})
    
    print blog_items
    return HttpResponse(json.dumps(blog_items,cls=QuerySetEncoder))


class UEditorTestModelForm(UEditorModelForm):
    class Meta:
        model = models.BlogAnswer

def blogSite(request,show_id):
    print 'show_id:',show_id
    bsCon=BlogContent.objects.filter(id=show_id)
    print bsCon
    for i in bsCon:
        print i.bc_Name
        
    form = UEditorTestModelForm()
    
    ba=BlogAnswer.objects.filter(ba_Id=show_id)
    for b in ba:
        print b.ba_Name
    """
    if request.method == 'POST':
        #M=Blog.objects.get(pk=1)
        form = UEditorTestModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('blog/blogshow.html', {'form': form,'blogcon':bsCon})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        try:
            M=BlogAnswer.objects.get(pk=1)
            form = UEditorTestModelForm(instance= M)
        except:
            form = UEditorTestModelForm(
                initial={'Description': '测试'}
            )
        #return render_to_response('test.html', {'form': form})
        """
    return render_to_response('blog/blogshow1.html',{'form': form,'blogcon':bsCon,'bloganswer':ba})
    
    
    
    