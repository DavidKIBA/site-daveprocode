from django import forms
from .models import Contacts
from services.models import Services

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ['nom', 'email_user_contact', 'telephone', 'ville', 'service', 'message']


    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nomUtilisateur', 'name':'nomUtilisateur'})
    )
    
    email_user_contact = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'name': 'email'})
    )

    telephone = forms.CharField(
        widget = forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'telephone', 'name': 'telephone', 'placeholder': 'Votre numéro de téléphone', 'min': '0', 'pattern': '[0-9]+'}
        )
    )

    ville = forms.CharField(
        widget= forms.TextInput(
        attrs={'class': 'form-control', 'id': 'ville', 'name': 'ville'}
        )
        
    )

    service = forms.ModelChoiceField(
        queryset=Services.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'services', 'name': 'services'})
    )

    message = forms.CharField(
        widget= forms.Textarea(
        attrs={'class': 'form-control', 'id': 'message', 'name': 'message', 'rows': "4"}
        )
    )
