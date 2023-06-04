from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .views import home, documento_listar, documento_crear, seguro_listar, seguro_crear

urlpatterns = [
    path("", home, name="home"),
    path("documento_listar/", documento_listar, name="mostraDoc"),
    path("documento_listar/crear_doc/", documento_crear, name="crearDoc"),
    path("seguro_listar/", seguro_listar, name="mostraSeg"),
    path("seguro_listar/crear_seg/", seguro_crear, name="crearSeg"),
]