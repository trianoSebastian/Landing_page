from django.db import models

class Mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)