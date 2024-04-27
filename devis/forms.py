from django import forms
from .models import Devis

class DevisForm(forms.ModelForm):
    class Meta:
        model = Devis
        fields = ['nom', 'email', 'service', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control bg-light border-0', 'style': 'height: 55px', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0', 'style': 'height: 55px', 'placeholder': 'E-mail'}),
            'service': forms.Select(attrs={'class': 'form-select bg-light border-0', 'style': 'height: 55px'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-light border-0', 'rows': 3, 'placeholder': 'Message'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].initial = 'Design'