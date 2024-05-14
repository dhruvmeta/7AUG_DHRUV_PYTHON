from django.contrib import admin
from django.urls import path, include
from dhruvapp import views

urlpatterns = [
    
    path ('getall/',views.getall),
    path ('getid/<int:id>',views.getid),
    path ('deleteid/<int:id>',views.deleteid)

]
