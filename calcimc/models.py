from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    peso = models.FloatField()
    altura = models.FloatField()
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('feminino', 'Feminino'), ('outro', 'Outro')])


class Historico(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name='historicos')
    nome = models.CharField(max_length=150, default="Usuário")
    peso = models.FloatField()
    altura = models.FloatField()
    imc = models.FloatField()
    status = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
