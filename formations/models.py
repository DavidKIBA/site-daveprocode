from django.db import models
from django.template.defaultfilters import slugify
import os

# Create your models here.


def rename_img(instance, filename):
    upload_to = "media/"
    extension = filename.split(".")[-1]
    if instance.titre:
        name = instance.titre.lower().replace(' ', '_')
        filename = (f"formation/{name}.{extension}")
        return os.path.join(upload_to, filename)


class Formations(models.Model):
    titre = models.CharField(max_length=255)
    image = models.ImageField(upload_to=rename_img)
    mini_description = models.TextField()
    description = models.TextField()
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = "Formation"
        verbose_name_plural = "Formations"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.titre