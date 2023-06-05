from django.shortcuts import render, redirect
from .models import Tipo_Documento_Identidad, tipos_seguro, paciente, especialidades, doctores

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

def documento_eliminar(request, document_id):
    documentos = Tipo_Documento_Identidad.objects.get(tipo_documento_id=document_id)
    documentos.delete()
    return redirect('/documento_listar/')

def seguro_listar(request):
    seguros = tipos_seguro.objects.all()
    return render(request, 'clinica_list/listar_tipos_seguro.html', {'tiposSeguro':seguros})

def seguro_crear(request):
    seguros = tipos_seguro(tipo_seguro_id=request.POST['seg_id'], tipo_seguro_nombre=request.POST['seg_name'])
    seguros.save()
    return redirect('/seguro_listar/')

def seguro_eliminar(request, seguro_id):
    seguros = tipos_seguro.objects.get(tipo_seguro_id=seguro_id)
    seguros.delete()
    return redirect('/seguro_listar/')

def pacientes_listar(request):
    pacientes = paciente.objects.all()
    tipos_documento = Tipo_Documento_Identidad.objects.all()
    tipos_seguros = tipos_seguro.objects.all()
    return render(request, 'clinica_list/listar_pacientes.html', {'pacientes': pacientes, 'tipos_documento': tipos_documento, 'tipos_seguros':tipos_seguros})

def pacientes_crear(request):
    tipo_documento_id = request.POST['tipo_documento_id']
    tipo_documento = Tipo_Documento_Identidad.objects.get(tipo_documento_id=tipo_documento_id)
    
    tipo_seguro_id = request.POST['tipo_seguro_id']
    tipo_seguro = tipos_seguro.objects.get(tipo_seguro_id=tipo_seguro_id)
    
    pacientes = paciente(
        tipo_documento_id=tipo_documento,
        nro_documento=request.POST['nro_documento'],
        nombre=request.POST['nombre'],
        apellidos=request.POST['apellidos'],
        direccion=request.POST['direccion'],
        fecha_nacimiento=request.POST['fecha_nacimiento'],
        tipo_seguro_id=tipo_seguro
    )
    
    pacientes.save()

    return redirect('/pacientes_listar/')

def pacientes_eliminar(request,paciente_id):
    pacientes = paciente.objects.get(id=paciente_id)
    pacientes.delete()
    return redirect('/pacientes_listar/')

def especialidad_listar(request):
    especialidad = especialidades.objects.all()
    return render(request, 'clinica_list/listar_especialidad.html', {'Especialidades':especialidad})

def especialidad_crear(request):
    especialidad = especialidades(especialidad_id=request.POST['esp_id'], especialidad_nombre=request.POST['esp_name'])
    especialidad.save()
    return redirect('/especialidad_listar/')

def especialidad_eliminar(request, especialidad_ID):
    especialidad = especialidades.objects.get(especialidad_id=especialidad_ID)
    especialidad.delete()
    return redirect('/especialidad_listar/')

def doctor_listar(request):
    doctor = doctores.objects.all()
    return render(request, 'clinica_list/listar_doctor.html', {'Doctores':doctor})

def doctor_crear(request):
    doctor = doctores(doctor_id=request.POST['doct_id'], doctor_nombre=request.POST['doct_name'])
    doctor.save()
    return redirect('/doctor_listar/')

def doctor_eliminar(request, doctor_ID):
    doctor = doctores.objects.get(doctor_id=doctor_ID)
    doctor.delete()
    return redirect('/doctor_listar/')
