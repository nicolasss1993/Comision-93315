from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from usuarios.views import *

urlpatterns = [
    path("login/", LoginView.as_view(template_name="usuarios/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="logout"),
    path("registro/", registro, name="registro"),
    path("usuario/datos", detalle_usuario, name="detalle_usuario"),
    path("usuario/actualizar_datos", actualizacion_usuario, name="actualizacion_usuario"),
]