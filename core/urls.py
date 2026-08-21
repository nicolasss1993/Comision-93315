from django.urls import path
from core.views import *


urlpatterns = [
    path("", home, name="home"),  # www.mercadolibre.com.ar/
    path("depas/", departamentos_medicos, name="listar_depas"),
    path("ver_depa/<int:nro_departamento>", ver_departamento, name="ver_depa"),
    
]
