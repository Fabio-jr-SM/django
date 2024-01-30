from app_cad_usuario import views
from django.urls import path

urlpatterns = [
    #rota, viwes responsavel, nome de referencia
    path('',views.home,name='home'),

    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
