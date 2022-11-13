from django.shortcuts import render
from django.http import HttpResponse
from .models import Correspondencia
from .models import Residencia

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')

def residencias(request):
    residencia = Residencia.objects.filter().order_by("number")
    search = (request.GET.get("search"))
    
    if search:
        residencia = Residencia.objects.filter(number = search).distinct()
    
    if search == "":
        residencia = Residencia.objects.filter().order_by("number")
    return render(request,'core/residencias.html', {'residencia': residencia})

def correspondencia(request):
    correspondencia = Correspondencia.objects.filter().order_by("residencia")
    search = (request.GET.get("search"))
    
    if search:
        correspondencia = Correspondencia.objects.filter(residencia = search).distinct()
    
    if search == "":
        correspondencia = Correspondencia.objects.filter().order_by("residencia")
    return render(request,'core/correspondencia.html', {'correspondencia': correspondencia, 'search': search})