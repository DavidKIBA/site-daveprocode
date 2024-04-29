from django.contrib import admin
from .models import Contacts, NewsLetters

# Register your models here.

class AdminContact(admin.ModelAdmin):
    list_display = ['nom', 'email_user_contact', 'ville', 'date']


admin.site.register(Contacts, AdminContact)
admin.site.register(NewsLetters)