from django.shortcuts import render
import random

def home(resquest):
    dados = {
        'nomes':['Tayane','Fabio','Claudinha'],
        'numero': random.randint(0,20)
    }
    return render(resquest,'index.html',dados)