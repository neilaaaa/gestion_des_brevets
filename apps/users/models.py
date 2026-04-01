from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    nom_role = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"
    def __str__(self):
        return self.nom_role


class Utilisateur(AbstractUser):
    date_ajout = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return self.username