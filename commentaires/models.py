from django.db import models
from services.models import Services
from utilisateurs.models import Utilisateurs

# Create your models here.


class Commentaires(models.Model):
    email_user_commentaire = models.EmailField()
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.email_user_commentaire
