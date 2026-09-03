from django.db import models
import uuid


def generar_code():
    return uuid.uuid4().hex


class Especialidades(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    fecha_de_ingreso = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=32, unique=True, default=generar_code)
    especialidad = models.ForeignKey(
        Especialidades,
        on_delete=models.SET_NULL,
        null=True,
        related_name="medicos"
    )  # FK
    
    def __str__(self):
        return f"{self.apellido}, {self.nombre} / {self.matricula}"
