from django.db import models
from services.models import Services
from utilisateurs.models import Utilisateurs

# Create your models here.


class Commandes(models.Model):

    STATUE = [
        ('attente', 'en attente'),
        ('non livré', 'non livré'),
        ('livré', 'livré'),
    ]

    username = models.ForeignKey(Utilisateurs, on_delete=models.CASCADE)
    statue_commande = models.CharField(max_length = 255, choices=STATUE, default='attente')
    quantite = models.PositiveSmallIntegerField()
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, to_field='nom')
    date_commande = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Commande"
        verbose_name_plural = "Commandes"

    def __str__(self):
        return self.id_commande
