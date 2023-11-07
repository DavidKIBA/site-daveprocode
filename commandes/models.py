from django.db import models
from services.models import Services
from utilisateurs.models import Utilisateurs

# Create your models here.


class Commande(models.Model):

    STATUE = {
        'attente': 'en attente',
        'non livré': 'non livré',
        'livré': 'livré',
    }

    id_commande = models.AutoField(primary_key=True)
    username = models.ForeignKey(Utilisateurs, on_delete=True)
    statue_commande = models.CharField(choices=STATUE, default='attente')
    quantite = models.PositiveSmallIntegerField()
    service = models.ForeignKey(
        Services, on_delete=models.CASCADE, to_field='nom')
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_commande
