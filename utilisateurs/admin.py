from django.contrib import admin
from .models import Utilisateurs, NewsLetters

# Register your models here.

admin.site.register(Utilisateurs)
admin.site.register(NewsLetters)

