from django.db import models

# Create your models here.
from django.db import models
from users.models import usuario

# Create your models here.
class Tipo_Documento_Identidad(models.Model):
    tipo_documento_id = models.CharField(max_length=25, primary_key=True)
    tipo_documento_nombre=models.CharField(max_length=150, null=False)

    REQUIRED_FIELD = ["tipo_documento_nombre"]

    class Meta:
        db_table = "tipo_documento_identidad"


class tipos_seguro(models.Model):
    tipo_seguro_id = models.CharField(max_length=25, primary_key=True)
    tipo_seguro_nombre=models.CharField(max_length=150, null=False)

    REQUIRED_FIELD = ["tipo_seguro_nombre"]

    class Meta:
        db_table = "tipos_seguro"


class paciente(models.Model):
    tipo_documento_id=models.ForeignKey(Tipo_Documento_Identidad, on_delete=models.CASCADE)
    nro_documento=models.CharField(max_length=10, null=False)
    nombre=models.CharField(max_length=100, null=False)
    apellidos=models.CharField(max_length=100, null=False)
    direccion=models.CharField(max_length=100, null=False)
    fecha_nacimiento=models.DateField()
    tipo_seguro_id=models.ForeignKey(tipos_seguro, on_delete=models.CASCADE)

    REQUIRED_FIELD = ["tipo_documento_id", "nro_documento", "nombre", "apellidos", "direccion", "fecha_nacimiento", "tipo_seguro_id"]

    class Meta:
        db_table="paciente"