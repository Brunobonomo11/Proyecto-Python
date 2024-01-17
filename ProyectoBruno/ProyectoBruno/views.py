from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime as dt
import random

def bienvenido(request):
    return HttpResponse('Hola, bienvenido a mi página')



def hora_actual(request):
    
    ahora = dt.datetime.now()
    
    mensaje = f"La hora actual es: {ahora.hour}:{ahora.minute}:{ahora.second}"
    
    return HttpResponse(mensaje)


def saludar(request, nombre):
    mensaje = f"Hola {nombre}, Mucho gusto"
    
    return HttpResponse(mensaje)


def inicio(request):
    
    #f = open("C:/Programacion-Bruno/Proyecto Pyhton/ProyectoBruno/ProyectoBruno/Templates/inicio.html")
    #plantilla = Template(f.read())
    #f.close()
    #aleatorio = random.randint(1,100)
    #info = {"numero":aleatorio}
    #contexto = Context(info)
    #plantilla = plantilla.render(contexto)
    
    plantilla = loader.get_template("inicio.html")
    aleatorio = random.randint(1,100)
    info = {"numero":aleatorio}
    plantilla = plantilla.render(info)
    
    return HttpResponse(plantilla)