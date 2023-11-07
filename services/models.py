from django.db import models

# Create your models here.


class Services(models.Model):
    id_services = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom
