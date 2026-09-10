from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from usuarios.forms import *


def registro(request):
    if request.method == "POST":
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("detalle_usuario")
    else:
        form = UsuarioCreateForm()
    return render(request, "usuarios/registro.html", {"form": form})


@login_required
def detalle_usuario(request):
    return render(request, "usuarios/detalle_usuario.html", {"user": request.user})

@login_required
def actualizacion_usuario(request):
    if request.method == "POST":
        form = UsuarioChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("detalle_usuario")
    else:
        form = UsuarioChangeForm(instance=request.user)
    
    return render(request, "usuarios/actualizar_usuario.html", {"form": form})
