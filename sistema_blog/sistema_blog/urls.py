from django.urls import path
from app_blog import views

urlpatterns = [
    path('', views.index_page),
]
