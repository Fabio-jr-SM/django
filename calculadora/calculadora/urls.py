from django.urls import path    
from app_calculadora import views
from django.http import HttpResponse

def soma(request, num1, num2):
    return HttpResponse(f'{num1+num2}')

urlpatterns = [
    path('soma/<int:num1>/<int:num2>/', soma),
]
