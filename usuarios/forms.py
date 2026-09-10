from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuario


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email")


class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ("avatar", "fecha_de_nacimiento", "pais", "direccion", "last_name", "first_name", "password")
        widgets = {
            "avatar": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_de_nacimiento": forms.DateInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"})
        }
