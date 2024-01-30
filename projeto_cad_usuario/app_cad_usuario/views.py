from django.shortcuts import render
from .models import Usuario
def home(resquest):
    return render(resquest,'usuarios/home.html')

def usuarios(resquest):
    novo_usuario = Usuario()
    novo_usuario.nome =  resquest.POST.get('nome')
    novo_usuario.idade = resquest.POST.get('idade')
    
    novo_usuario.save()

    #Exibir informações em uma nova Pagina

    usuarios = {
        'usuarios':Usuario.objects.all()
    }

    #retornar os dados para a pagina para a listagem de user

    return render(resquest,'usuarios/usuarios.html',usuarios)