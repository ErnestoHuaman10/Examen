from django.shortcuts import render, redirect
from .models import Tipo_Documento_Identidad, tipos_seguro, paciente

# Create your views here.
def home(request):
    return render(request, "home.html")

def documento_listar(request):
    documentos = Tipo_Documento_Identidad.objects.all()
    return render(request, 'clinica_list/listar_documento_identidad.html', {'documentoIdentidad':documentos})


def documento_crear(request):
    documento = Tipo_Documento_Identidad(tipo_documento_id=request.POST['doc_id'], tipo_documento_nombre=request.POST['doc_name'])
    documento.save()
    return redirect('/documento_listar/')

def seguro_listar(request):
    seguros = tipos_seguro.objects.all()
    return render(request, 'clinica_list/listar_tipos_seguro.html', {'tiposSeguro':seguros})

def seguro_crear(request):
    documento = tipos_seguro(tipo_seguro_id=request.POST['seg_id'], tipo_seguro_nombre=request.POST['seg_name'])
    documento.save()
    return redirect('/seguro_listar/')