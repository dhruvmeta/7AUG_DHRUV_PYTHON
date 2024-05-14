from django.contrib import admin
from .models import *

# Register your models here.
 
class bdata(admin.ModelAdmin):
    list_display=['title','author','isbn','publisher']
    

admin.site.register(Book,bdata)
