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
        
    def clean_email(self):
        email = self.cleaned_data["email"]
        
        if not email.endswith("@hospital.com"):
            raise forms.ValidationError(
                "El email debe pertenecer al dominio del hospital. Ej: Laboratorio@hospital.com"
            )

        return email
    
    def clean_nro_departamento(self):
        nro = self.cleaned_data["nro_departamento"]
        
        if DepartamentosMedicos.objects.filter(
            nro_departamento=nro
        ).exists():
            raise forms.ValidationError("El numero de departamento esta en uso.")

        return nro


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
