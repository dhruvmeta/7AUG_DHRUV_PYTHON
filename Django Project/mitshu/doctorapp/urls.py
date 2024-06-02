from django.contrib import admin
from django.urls import path,include
from doctorapp import views

urlpatterns = [
    path('',views.index),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    
]
