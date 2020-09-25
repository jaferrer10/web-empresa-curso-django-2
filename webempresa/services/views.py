from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):

    #arriba importamos el modelo de datos y aqui traemos todos los registros
    services = Service.objects.all()
    return render(request, "services/services.html", {'services':services})
