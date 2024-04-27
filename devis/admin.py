from django.contrib import admin
from .models import Devis

# Register your models here.

class AdminDevis(admin.ModelAdmin):
    list_display = ["nom", "email", "service", "date_ajoute"]

admin.site.register(Devis, AdminDevis)