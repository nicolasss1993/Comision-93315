from django.db import models
from django.contrib.auth.models import AbstractUser


def avatar_upload_to(instance, filename):
    return f"avatars/{instance.username}/{filename}"


class Usuario(AbstractUser):
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    avatar = models.ImageField(
        upload_to=avatar_upload_to,
        blank=True,
        null=True,
        default="default/default.png"
    )

    def __str__(self):
        return f"{self.username}: {self.last_name}, {self.first_name}"
