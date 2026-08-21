from django.shortcuts import render, get_object_or_404
from core.models import DepartamentosMedicos



def home(request):
    return render(request, "core/index.html")


def departamentos_medicos(request):
    depas = DepartamentosMedicos.objects.all() # QuerySet([..., ..., ...,])
    print(depas)
    contexto = {
        "departamentos_list": list(depas)
    }
    print(contexto)
    return render(request, "core/departamentos.html", contexto)


def ver_departamento(request, nro_departamento):
    depa = get_object_or_404(DepartamentosMedicos, nro_departamento=nro_departamento)
    contexto = {
        "depa": depa
    }

    return render(request, "core/ver_depa.html", contexto)
