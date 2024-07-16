from django.shortcuts import render
#from .models import Curso
from django.http import HttpResponse
# Create your views here.

""""
def crear_curso(request):
    nombre=input("Ingrese el nombre del curso: ")
    comision=input("Ingrese el numero de comicion")
    curso=Curso(nombre=nombre,comision=comision)
    curso.save()
    text= f"Curso Creado y registrado"
    return HttpResponse(text)

def mostrar_cursos(request):
    cursos=Curso.objects.all()
    
    contexto={"Cursos":cursos}
    
    return render(request,"cursos.html",contexto)
    
"""
def inicio(request):
    return render(request,"appcoder/inicio.html")

def cursos(request):
    return render(request,"appcoder/cursos.html")

def estudiantes(request):
    return render(request,"appcoder/estudiantes.html")

def profesores(request):
    return render(request,"appcoder/profesores.html")


def entregables(request):
    return render(request,"appcoder/entregables.html")


