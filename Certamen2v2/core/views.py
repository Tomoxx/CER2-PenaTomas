from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.utils import timezone
from core.models import Correspondencia

# Create your views here.
def inicio(request):
    return render(request,'core/inicio.html')

def residencias(request):
    return render(request,'core/residencias.html')

def correspondencia(request):
    return render(request,'core/correspondencia.html')

class CorrespondenciaList(ListView):
    model = Correspondencia
    paginate_by: 25
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context