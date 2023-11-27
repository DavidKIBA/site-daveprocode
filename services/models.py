from django.db import models

# Create your models here.


class Services(models.Model):
    nom = models.CharField(max_length=255, unique=True)
    prix_normal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prix_discutable = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.nom
