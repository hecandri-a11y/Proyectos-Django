from django.shortcuts import render

# Create your views here.

#Definimos una función para la url
def index(request):

    return render(request, 'alumnos/index.html')

def arte(request):
    return render(request, 'alumnos/html/arte.html')

def deporte(request):
    return render(request, 'alumnos/html/deporte.html')

def dibujo(request):
    return render(request, 'alumnos/html/dibujo.html')

def pintura(request):
    return render(request, 'alumnos/html/pintura.html')

def escultura(request):
    return render(request, 'alumnos/html/escultura.html')

def futbol(request):
    return render(request, 'alumnos/html/futbol.html')

def basquetbol(request):
    return render(request, 'alumnos/html/basquetbol.html')

def natacion(request):
    return render(request, 'alumnos/html/natacion.html')

def Contacto(request):
    return render(request, 'alumnos/html/Contacto.html')

def formulariodeprueba(request):
    return render(request, 'alumnos/html/formulariodeprueba.html')

def localstore(request):
    return render(request, 'alumnos/html/localstore.html')

def AnaTorres(request):
    return render(request, 'alumnos/html/AnaTorres.html')

def AntonioVirgolini(request):
    return render(request, 'alumnos/html/AntonioVirgolini.html')

def CarlosSoto(request):
    return render(request, 'alumnos/html/CarlosSoto.html')

def CristobalSancho(request):
    return render(request, 'alumnos/html/CristobalSancho.html')

def EnzoSanchez(request):
    return render(request, 'alumnos/html/EnzoSanchez.html')

def GuillermoGomez(request):
    return render(request, 'alumnos/html/GuillermoGomez.html')

def JuanMartinez(request):
    return render(request, 'alumnos/html/JuanMartinez.html')

def JuanPerez(request):
    return render(request, 'alumnos/html/JuanPerez.html')

def MarcusAnton(request):
    return render(request, 'alumnos/html/MarcusAnton.html')

def MariaLopez(request):
    return render(request, 'alumnos/html/MariaLopez.html')

def MartinAlejandro(request):
    return render(request, 'alumnos/html/MartinAlejandro.html')

def MatildaAlejandra(request):
    return render(request, 'alumnos/html/MatildaAlejandra.html')

def SelenaMichell(request):
    return render(request, 'alumnos/html/SelenaMichell.html')

def VictoriaPerez(request):
    return render(request, 'alumnos/html/VictoriaPerez.html')