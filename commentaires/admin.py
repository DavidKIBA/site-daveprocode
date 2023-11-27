from django.contrib import admin
from .models import Commentaires

# Register your models here.

class AdminCommentaires(admin.ModelAdmin):
    list_display = ['email_user_commentaire', 'contenu', 'date']

admin.site.register(Commentaires, AdminCommentaires)
