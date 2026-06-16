from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Categorías
    path('arte/', views.arte, name='arte'),
    path('deporte/', views.deporte, name='deporte'),

    # Talentos de arte
    path('dibujo/', views.dibujo, name='dibujo'),
    path('pintura/', views.pintura, name='pintura'),
    path('escultura/', views.escultura, name='escultura'),

    # Talentos de deporte
    path('futbol/', views.futbol, name='futbol'),
    path('basquetbol/', views.basquetbol, name='basquetbol'),
    path('natacion/', views.natacion, name='natacion'),

    # Formularios
    path('contacto/', views.Contacto, name='Contacto'),
    path('formulariodeprueba/', views.formulariodeprueba, name='formulariodeprueba'),
    path('localstore/', views.localstore, name='localstore'),

    # Fichas individuales
    path('AnaTorres/', views.AnaTorres, name='AnaTorres'),
    path('AntonioVirgolini/', views.AntonioVirgolini, name='AntonioVirgolini'),
    path('CarlosSoto/', views.CarlosSoto, name='CarlosSoto'),
    path('CristobalSancho/', views.CristobalSancho, name='CristobalSancho'),
    path('EnzoSanchez/', views.EnzoSanchez, name='EnzoSanchez'),
    path('GuillermoGomez/', views.GuillermoGomez, name='GuillermoGomez'),
    path('JuanMartinez/', views.JuanMartinez, name='JuanMartinez'),
    path('JuanPerez/', views.JuanPerez, name='JuanPerez'),
    path('MarcusAnton/', views.MarcusAnton, name='MarcusAnton'),
    path('MariaLopez/', views.MariaLopez, name='MariaLopez'),
    path('MartinAlejandro/', views.MartinAlejandro, name='MartinAlejandro'),
    path('MatildaAlejandra/', views.MatildaAlejandra, name='MatildaAlejandra'),
    path('SelenaMichell/', views.SelenaMichell, name='SelenaMichell'),
    path('VictoriaPerez/', views.VictoriaPerez, name='VictoriaPerez'),
]