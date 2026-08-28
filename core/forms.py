from django import forms
from core.models import DepartamentosMedicos


class DepartamentosMedicosForm(forms.ModelForm):
    class Meta:
        model = DepartamentosMedicos
        fields = ("nombre", "nro_departamento", "cantidad_medicos", "email")
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nombre"
            }),
            "nro_departamento": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nro de depa"
            }),
            "cantidad_medicos": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese la cantidad de medicos"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el email"
            })
        }


class DepartamentosMedicosUpdateForm(forms.ModelForm):
    class Meta:
        model = DepartamentosMedicos
        fields = ("nombre", "cantidad_medicos", "email")
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el nombre"
            }),
            "cantidad_medicos": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese la cantidad de medicos"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Ingrese el email"
            })
        }
