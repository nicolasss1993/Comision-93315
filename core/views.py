from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import DepartamentosMedicos
from core.forms import DepartamentosMedicosForm, DepartamentosMedicosUpdateForm


def home(request):
    return render(request, "core/index.html")


@login_required
def departamentos_medicos(request):
    nombre = request.GET.get("nombre")
    depas = DepartamentosMedicos.objects.all() # QuerySet([..., ..., ...,])
    if nombre is not None:
        depas = depas.filter(nombre__icontains=nombre)

    contexto = {
        "departamentos_list": list(depas)
    }

    return render(request, "core/departamentos.html", contexto)


@login_required
def ver_departamento(request, nro_departamento):
    depa = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)
    contexto = {
        "depa": depa
    }

    return render(request, "core/ver_depa.html", contexto)


# CRUD
# Create - Crear /
# Read - Leer /
# Update - Actualizar
# Delete - Eliminar

# GET - Se pide informacion al servidor
# POST - Crear informacion / Editar informacion.
# PUT - Editar/Actualizar informacion /// DRF Django Rest Framework
# DELETE - Eliminar info

@login_required
def crear_depa(request):
    if request.method == "POST":
        form = DepartamentosMedicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar_depas")
    else: # elif request.method == "GET"
        form = DepartamentosMedicosForm()
    
    return render(request, "core/crear_depa.html", {"form": form})

@login_required
def editar_departamento(request, nro_departamento):
    depa = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)
    
    if request.method == "POST":
        form = DepartamentosMedicosUpdateForm(request.POST, instance=depa)
        if form.is_valid():
            form.save()
            return redirect("ver_depa", nro_departamento=nro_departamento)
    else:
        form = DepartamentosMedicosUpdateForm(instance=depa)
    
    return render(request, "core/editar_depa.html", {
        "form": form,
        "depa": depa
    })


@login_required
def consulta_eliminar_depa(request, nro_departamento):
    return render(request, "core/eliminar_depa.html", {"nro_departamento": nro_departamento})

@login_required
def elimar_depa(request, nro_departamento):
    depa = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)

    if request.method == "POST":
        depa.delete()
        return redirect("listar_depas")
