from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def cadastro(request):
    return render(request,'cadastro.html')


def login(request):
    return render(request,'login.html')