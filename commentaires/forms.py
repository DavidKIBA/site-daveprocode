from .models import Commentaires
from django import forms


class CommentairesForm(forms.ModelForm):

    class Meta:
        model = Commentaires
        fields = ['email_user_commentaire', 'contenu']

    email_user_commentaire = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp'})
    )

    contenu = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleInputMessage', 'rows': '3'})
    )