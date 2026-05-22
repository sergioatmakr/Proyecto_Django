from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título de la receta")
    descripcion = models.TextField(verbose_name="Descripción corta/Resumen")
    ingredientes = models.TextField(help_text="Escribe los ingredientes separados por líneas.")
    instrucciones = models.TextField(verbose_name="Pasos de preparación")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recetas')

    def __str__(self):
        return self.titulo