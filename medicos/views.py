from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) # FORMAN UN CRUD / Create Read Update Delete
from medicos.models import Medico
from django.contrib.auth.mixins import LoginRequiredMixin


class MedicoListView(ListView):
    model = Medico
    template_name = "medicos/medicos_list.html"
    context_object_name = "medico_list"

    def get_queryset(self):
        consulta = super().get_queryset() # Medico.objects.all()
        nombre = self.request.GET.get("nombre")
        
        if nombre is not None:
            consulta = consulta.filter(nombre__icontains=nombre)
        
        return consulta


class MedicoDetailView(DetailView):
    model = Medico
    template_name = "medicos/medicos_detail.html"
    context_object_name = "medico"
    slug_field = "code"
    slug_url_kwarg = "code"


class MedicoCreateView(CreateView):
    model = Medico
    fields = ("nombre", "apellido", "matricula", "email", "especialidad")
    template_name = "medicos/medico_create.html"
    
    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )


class MedicoUpdateView(UpdateView):
    model = Medico
    fields = ("nombre", "apellido", "matricula", "email")
    slug_field = "matricula"
    slug_url_kwarg = "matricula"
    template_name = "medicos/medico_update.html"

    def get_success_url(self):
        return reverse_lazy(
            "medico_detail",
            kwargs={"code": self.object.code}
        )


class MedicoDeleteView(DeleteView):
    model = Medico
    template_name = "medicos/medico_confirm_delete.html"
    success_url = reverse_lazy("medico_list")
    slug_field = "code"
    slug_url_kwarg = "code"
