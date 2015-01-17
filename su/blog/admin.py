#!/usr/bin/env python
#coding=utf-8
from django.contrib import admin

# Register your models here.
from blog.models import *


class FirstMenuAdmin(admin.ModelAdmin):
    list_display=('first_menu','first_remark')
    search_fields=('first_menu',)
    ordering=('-first_menu_date',)
    
class SecondMenuAdmin(admin.ModelAdmin):
    list_display=('second_menu','parent_menu','second_remark')
    list_filter=('parent_menu',)
    search_fields=('parent_menu',)
    ordering=('-parent_menu',)
    
class BlogContentAdmin(admin.ModelAdmin):
    list_display=('bc_Name','bc_Description','bc_Datetime')
    list_filter=('bc_Datetime',)
    search_fields=('bc_Name','bc_Style')
    
class BlogAnswerAdmin(admin.ModelAdmin):
    list_display=('ba_Id','ba_Name','ba_Datetime','ba_Content')
    list_filter=('ba_Name','ba_Datetime')
    search_fields=('ba_Name',)
    


admin.site.register(BlogAnswer,BlogAnswerAdmin)
admin.site.register(FirstMenu,FirstMenuAdmin)
admin.site.register(SecondMenu,SecondMenuAdmin)
admin.site.register(BlogContent,BlogContentAdmin)
