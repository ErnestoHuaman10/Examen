from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import home, documento_listar, documento_crear,documento_eliminar, seguro_listar, seguro_crear, seguro_eliminar, pacientes_listar, pacientes_crear, pacientes_eliminar,especialidad_listar,especialidad_crear,especialidad_eliminar,doctor_listar,doctor_crear,doctor_eliminar
urlpatterns = [
    path("", home, name="home"),
    path("documento_listar/", documento_listar, name="mostraDoc"),
    path("documento_listar/crear_doc/", documento_crear, name="crearDoc"),
    path('eliminar_documento/<int:document_id>/', documento_eliminar, name='eliminar_documento'),
    
    path("seguro_listar/", seguro_listar, name="mostraSeg"),
    path("seguro_listar/crear_seg/", seguro_crear, name="crearSeg"),
    path('eliminar_seguro/<int:seguro_id>/', seguro_eliminar, name='eliminar_seguro'),
    
    path("pacientes_listar/", pacientes_listar, name="mostraPaciente"),
    path("pacientes_listar/crear_pacientes/", pacientes_crear, name="crearPaciente"),
    path('eliminar_paciente/<int:paciente_id>/', pacientes_eliminar, name='eliminar_paciente'),
    
    path("especialidad_listar/", especialidad_listar, name="mostraEsp"),
    path("especialidad_listar/crear_esp/", especialidad_crear, name="crearEsp"),
    path('eliminar_especialidad/<int:especialidad_ID>/', especialidad_eliminar, name='eliminar_especialidad'),
    
    path("doctor_listar/", doctor_listar, name="mostraDoct"),
    path("doctor_listar/crear_doct/", doctor_crear, name="crearDoct"),
    path('eliminar_doctor/<int:doctor_ID>/', doctor_eliminar, name='eliminar_doctor'),
]