from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('historico/', views.historico, name='historico'),
    path('login/', views.login_view, name='login'),
    path('salvar_imc/', views.salvar_imc, name='salvar_imc'),
    path('grafico_historico/', views.grafico_historico, name='grafico_historico')
]