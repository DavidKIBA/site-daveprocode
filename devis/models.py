from django.db import models
from services.models import Services

# Create your models here.

class Devis(models.Model):

    nom = models.CharField(max_length=255)
    email = models.EmailField()
    service = models.ForeignKey(Services, on_delete=models.SET_NULL, null=True, default=1)
    message = models.TextField()
    date_ajoute = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Devi"
        verbose_name_plural = "Devis"

    
