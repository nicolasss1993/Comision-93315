from django.contrib import admin
from core.models import DepartamentosMedicos


#admin.site.register(DepartamentosMedicos)

@admin.register(DepartamentosMedicos)
class DepartamentosAdmin(admin.ModelAdmin):
    # Columnas visibles en la tabla de admin
    list_display = ("nombre", "nro_departamento", "fecha_creacion")

    # Campo clickeable para poder ingresar al registro completo
    list_display_links = ("nombre",)

    # Agrega el panel lateral de filtros
    list_filter = ("nro_departamento", "nombre")

    # Habilita la barra de busqueda sobre estos campos
    search_fields = ("nro_departamento", "email")

    # Orden por defecto de los registros
    ordering = ("nro_departamento", "email")

    # Campo de solo lectura
    readonly_fields = ("fecha_creacion",)
