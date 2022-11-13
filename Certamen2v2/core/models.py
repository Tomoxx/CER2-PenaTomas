from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Residencia(models.Model):
    number = models.IntegerField(primary_key=True)
    dueno = models.CharField(max_length=50)
    telefono = models.IntegerField()
    
    def __str__(self) -> str:
        return "Residencia "+ str(self.number)

class Correspondencia(models.Model):
    fechaRecibida = models.DateTimeField((""), auto_now=False, auto_now_add=False, default=now)
    conserje = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="Conserjes", limit_choices_to={'groups__name':"Conserjes"})
    remitente = models.CharField(max_length=50)
    NORECIBIDO = 'NR'
    RECIBIDO = 'R'
    estados = [(NORECIBIDO, 'No Recibido'), (RECIBIDO, 'Recibido')] 
    estado = models.CharField(max_length=15, choices=estados, default=NORECIBIDO,)
    destinatario = models.CharField(max_length=50)
    residencia = models.ForeignKey('Residencia', on_delete=models.SET_NULL, null=True)
    
    def __str__(self) -> str:
        return "Correspondencia para " + str(self.destinatario)

