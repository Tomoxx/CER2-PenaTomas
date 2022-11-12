from django.db import models
from django.utils.timezone import now

# Create your models here.
class Residencia(models.Model):
    number = models.IntegerField(primary_key=True)
    dueno = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Correspondencia(models.Model):
    fechaRecibida = models.DateTimeField((""), auto_now=False, auto_now_add=False, default=now)
    recibidor = models.CharField(max_length=50)
    remitente = models.CharField(max_length=50)
    NORECIBIDO = 'NR'
    RECIBIDO = 'R'
    estados = [(NORECIBIDO, 'No recibido'), (RECIBIDO, 'Recibido')] 
    estado = models.CharField(max_length=2, choices=estados, default=NORECIBIDO,)
    destinatario = models.CharField(max_length=50)
    residencia = models.ForeignKey('Residencia', on_delete=models.CASCADE)
