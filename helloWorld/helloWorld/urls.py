from django.contrib import admin
from django.urls import path
from app_helloWorld import views

urlpatterns = [
    path('', views.home),
]
