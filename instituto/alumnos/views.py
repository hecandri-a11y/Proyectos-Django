from django.shortcuts import render

# Create your views here.

#Definimos una función para la url
def index(request):

    return render(request, 'alumnos/index.html')