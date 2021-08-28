from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from datetime import datetime

class User(AbstractUser):
    pass

class Pregunta(models.Model):
    texto = models.TextField(max_length=400)

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    texto = models.CharField(max_length=255)

    es_correcta = models.BooleanField()

class EstadisticasUsuarios(models.Model):
    """
    cantidad de usuarios.
    cantidad de partidas por dia. veremos
        en total de los ultima semana.
    conexiones por dia. veremos
        en total de los ultima semana.
    """
    cantidad_de_usuarios = models.IntegerField(default=0)

class LoginDetails(models.Model):
    login_time = models.DateTimeField(default=datetime.now(), blank=False)

class PartidasDetails(models.Model):
    time = models.DateTimeField(default=datetime.now(), blank=False)


class ProgresoSesion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    puntaje = models.IntegerField(default=0)

    vidas = models.IntegerField(default=3)

    def obtener_todas_las_preguntas():
        string_de_preguntas = ""

        preguntas = Pregunta.objects.all()

        for pregunta in preguntas:
            string_de_preguntas += str(pregunta.id) + ","
        
        return string_de_preguntas[:-1]

    preguntas_disponibles = models.CharField(max_length=255, default=obtener_todas_las_preguntas()) #una string con los id de las preguntas disponibles.

    primera_partida = models.BooleanField(default=True)

class ProgresoHistorico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    mejor_racha = models.IntegerField(default=0)

    puntaje_historico = models.IntegerField(default=0)



