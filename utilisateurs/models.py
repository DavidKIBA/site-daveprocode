from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Utilisateurs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"
    
    def __str__(self):
        return self.user

class NewsLetters(models.Model):
    id_email_news_letter = models.AutoField(primary_key=True)
    email_news_letter = models.EmailField()

    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"

    def __str__(self):
        return self.email_news_letter