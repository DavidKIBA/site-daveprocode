from django.db import models
from django.template.defaultfilters import slugify
import os


# Create your models here.

def rename_img(instance, filename):
    upload_to = "media/"
    extension = filename.split(".")[-1]
    if instance.titre:
        name = instance.titre.lower().replace(' ', '_')
        filename = (f"service/{name}.{extension}")
        return os.path.join(upload_to, filename)


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

class MiniService(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to=rename_img)
    mini_description = models.TextField()
    description = models.TextField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Mini Service"
        verbose_name_plural = "Mini Services"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.titre