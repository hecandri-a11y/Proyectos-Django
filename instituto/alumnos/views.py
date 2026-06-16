from django.shortcuts import render

# Create your views here.

#Definimos una función para la url
def index(request):

    return render(request, 'alumnos/index.html')

def arte(request):
    return render(request, 'html/arte.html')

def deporte(request):
    return render(request, 'html/deporte.html')

def dibujo(request):
    return render(request, 'html/dibujo.html')

def pintura(request):
    return render(request, 'html/pintura.html')

def escultura(request):
    return render(request, 'html/escultura.html')

def futbol(request):
    return render(request, 'html/futbol.html')

def basquetbol(request):
    return render(request, 'html/basquetbol.html')

def natacion(request):
    return render(request, 'html/natacion.html')

def Contacto(request):
    return render(request, 'html/Contacto.html')

def formulariodeprueba(request):
    return render(request, 'html/formulariodeprueba.html')

def localstore(request):
    return render(request, 'html/localstore.html')

def AnaTorres(request):
    return render(request, 'html/AnaTorres.html')

def AntonioVirgolini(request):
    return render(request, 'html/AntonioVirgolini.html')

def CarlosSoto(request):
    return render(request, 'html/CarlosSoto.html')

def CristobalSancho(request):
    return render(request, 'html/CristobalSancho.html')

def EnzoSanchez(request):
    return render(request, 'html/EnzoSanchez.html')

def GuillermoGomez(request):
    return render(request, 'html/GuillermoGomez.html')

def JuanMartinez(request):
    return render(request, 'html/JuanMartinez.html')

def JuanPerez(request):
    return render(request, 'html/JuanPerez.html')

def MarcusAnton(request):
    return render(request, 'html/MarcusAnton.html')

def MariaLopez(request):
    return render(request, 'html/MariaLopez.html')

def MartinAlejandro(request):
    return render(request, 'html/MartinAlejandro.html')

def MatildaAlejandra(request):
    return render(request, 'html/MatildaAlejandra.html')

def SelenaMichell(request):
    return render(request, 'html/SelenaMichell.html')

def VictoriaPerez(request):
    return render(request, 'html/VictoriaPerez.html')