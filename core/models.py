from django.db import models



class DepartamentosMedicos(models.Model):
    nombre = models.CharField(max_length=50)
    nro_departamento = models.IntegerField(unique=True)
    cantidad_medicos = models.IntegerField()
    fecha_creacion = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return f"Departamento: {self.nombre} / nro: {self.nro_departamento}"

