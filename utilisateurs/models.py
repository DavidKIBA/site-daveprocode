from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Utilisateurs(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.username
