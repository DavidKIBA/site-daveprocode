from django.db import models

# Create your models here.

class Contacts(models.Model):


    nom = models.CharField(max_length=255)
    email_user_contact = models.EmailField()
    telephone = models.CharField(max_length=15)
    ville = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom

class NewsLetters(models.Model):
    email_news_letter = models.EmailField()

    class Meta:
        verbose_name = "News Letter"
        verbose_name_plural = "News Letters"

    def __str__(self):
        return self.email_news_letter