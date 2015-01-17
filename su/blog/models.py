#!/usr/bin/env python
#coding=utf-8
from django.db import models
import datetime
from django.utils import timezone
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *

# Create your models here.
from DjangoUeditor.models import UEditorField



class FirstMenu(models.Model):
    '''一级分类'''
    first_menu=models.CharField('一级分类',max_length=30)
    first_remark=models.TextField('一级分类备注',null=True,blank=True)
    first_menu_date=models.DateTimeField('录入时间',default=datetime.datetime.now())
    #first_menu_date=models.DateTimeField('录入时间',auto_now_add=True)
    def __unicode__(self):
        return self.first_menu
    
    def was_published_recently(self):
        return self.first_menu_date >=timezone.now()-datetime.timedelta(days=1)
    
    class Meta:
        ordering=['first_menu_date']

class SecondMenu(models.Model):
    second_menu=models.CharField('二级分类',max_length=30)
    parent_menu=models.ForeignKey(FirstMenu,verbose_name='一级分类')
    second_remark=models.TextField('二级分类备注',null=True,blank=True)
    
    def __unicode__(self):
        return self.second_menu
    

        
def getImagePath(model_instance=None):
    if model_instance is None:
        return "aaa/"
    else:
        return "%s/" % model_instance.Name

def getDescImagePath(model_instance=None):
        return "aaa/"

class myEventHander(UEditorEventHandler):
    def on_selectionchange(self):
        return """
            function getButton(btnName){
                var items=%(editor)s.ui.toolbars[0].items;
                for(item in items){
                    if(items[item].name==btnName){
                        return items[item];
                    }
                }
            }
            var btn=getButton("mybtn1");
            var selRanage=id_Description.selection.getRange()
            btn.setDisabled(selRanage.startOffset == selRanage.endOffset);

        """

class myBtn(UEditorButtonCommand):
    def onClick(self):
        return u"""
            alert("爽!");
            editor.execCommand(uiName);
        """
    def onExecuteQueryvalueCommand(self):
        return """
            return 1;
        """
    def onExecuteAjaxCommand(self,state):
        if state=="success":
            return u"""
                alert("后面比较爽!"+xhr.responseText);
            """
        if state=="error":
            return u"""
                alert("讨厌，摸哪里去了！"+xhr.responseText);
            """
class myCombo(UEditorComboCommand):
    def onSelect(self):
        return u"""
            alert("选择了!");
        """
    def get_items(self):
        items=[]
        for i in xrange(10):
            items.append({
                "label":"combo_%s" % i,
                "value":i
            })
        return items

class BlogContent(models.Model):
    '''博客内容'''
    bc_Name = models.CharField(u'标题', max_length=100)
    bc_Mark=models.TextField(u'内容简介')
    bc_Description = UEditorField(u'描述', blank=True, toolbars="full", imagePath="cool/", settings={"a": 1},
                               command=[myBtn(uiName="mybtn1", icon="d.png", title=u"1摸我", ajax_url="/ajaxcmd/"),
                                       myCombo(uiName="myCombo3",title=u"ccc",initValue="aaa")],
                               event_handler=myEventHander())
    bc_Style=models.ManyToManyField(SecondMenu,verbose_name='类别')
    bc_Datetime=models.DateTimeField('录入时间',auto_now_add=True)
    def __unicode__(self):
        return self.bc_Name
    class Meta:
        ordering=['bc_Datetime']
        
        
class BlogAnswer(models.Model):
    '''评论'''
    ba_Id=models.ForeignKey(BlogContent,verbose_name='所属')
    ba_Name=models.CharField(u'用户名',max_length=30)
    ba_Datetime=models.DateTimeField('回复日期',default=datetime.datetime.now())
    ba_Content = UEditorField(u'内容', height=200, width=800, default='test', imagePath="answer/img/", toolbars="mini",
                           filePath='answers/files/', blank=True, settings={"a": 2})
    
    def __unicode__(self):
        return self.ba_Id
    
    class Meta:
        ordering=['ba_Datetime']
    
    