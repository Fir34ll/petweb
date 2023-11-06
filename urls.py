
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
     path('', views.index, name='index'),  # Exemplo de uma rota para a página inicial
    path('about/', views.about, name='about'),
    
]

