from django.db import models

# Create your models here.

class Produits(models.Model):

    id_product = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    prix_produit = models.DecimalField(max_digits=10, decimal_places=2)
    stock_produit = models.IntegerField()

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.nom_produit