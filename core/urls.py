from django.urls import path
from core.views import *


urlpatterns = [
    path("", home, name="home"),  # www.mercadolibre.com.ar/
    path("depas/", departamentos_medicos, name="listar_depas"),
    path("ver_depa/<int:nro_departamento>", ver_departamento, name="ver_depa"),
    path("editar_depa/<int:nro_departamento>", editar_departamento, name="editar_depa"),
    path("departamento/consulta_eliminar/<int:nro_departamento>", consulta_eliminar_depa, name="consulta_eliminar_depa"),
    path("departamento/eliminar/<int:nro_departamento>", elimar_depa, name="eliminar_depa"),
    path("crear_depa/", crear_depa, name="crear_depa"),
]
