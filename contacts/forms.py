from django import forms
from .models import Contacts
from services.models import Services

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['nom', 'email_user_contact', 'telephone', 'ville', 'message']


    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nomUtilisateur', 'name':'nomUtilisateur'})
    )
    
    email_user_contact = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email'})
    )

    telephone = forms.CharField(
        widget = forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'telephone', 'name': 'telephone',  'min': '0', 'pattern': '[0-9]+'}
        )
    )

    ville = forms.CharField(
        widget= forms.TextInput(
        attrs={'class': 'form-control', 'id': 'ville', 'name': 'ville'}
        )
        
    )

    message = forms.CharField(
        widget= forms.Textarea(
        attrs={'class': 'form-control', 'id': 'message', 'name': 'message', 'rows': '6', 'style': 'font-size: 14px', 'placeholder':'Comment pouvons-nous vous aider?' }
        )
    )
