from django.db import models
from services.models import Services

# Create your models here.

class Contacts(models.Model):

    # CHOICE_SERVICE = [
    #     ('dev', 'Developpement Web'),
    #     ('mar', 'Marketing Digital'),
    #     ('mai', 'Maintenance Informatique'),
    #     ('pho', 'Photographie & Vidéographie'),
    #     ('inf', 'Infographie'),
    #     ('des', 'Design')
    # ]

    nom = models.CharField(max_length=255)
    email_user_contact = models.EmailField()
    telephone = models.CharField(max_length=15)
    ville = models.CharField(max_length=30)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom
