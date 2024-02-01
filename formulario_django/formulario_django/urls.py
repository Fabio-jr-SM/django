from django.contrib import admin
from django.urls import path
from app_formulario import views

urlpatterns = [
    path('feed/', views.feed),
    path('publicate/', views.publicate),
]
