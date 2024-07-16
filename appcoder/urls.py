from django.urls import path
from appcoder.views import inicio,cursos,estudiantes,profesores,entregables


urlpatterns = [
    
    path('',inicio),
    path('Pagina-Cursos/',cursos),
    path('Estudiantes/',estudiantes),
    path('Profesores/',profesores),
    path('Entregables/',entregables),
    
]

    