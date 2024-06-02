from django.contrib import admin
from django.urls import path,include
from dhruvapp import views

urlpatterns = [
   path('',views.index),
]