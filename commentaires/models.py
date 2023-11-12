from django.db import models
from services.models import Services
from utilisateurs.models import Utilisateurs

# Create your models here.


class Commentaires(models.Model):
    id_commentaire = models.AutoField(primary_key=True)
    username = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    id_product_service = models.ForeignKey(
        Services, on_delete=models.CASCADE, null=True)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    def __str__(self):
        return self.contenu
