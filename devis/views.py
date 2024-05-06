from django.shortcuts import render, redirect
from .forms import DevisForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def devis_view(request):
    # form_devis = DevisForm()

    form_devis = DevisForm(request.POST)
    if form_devis.is_valid():
        form_devis.save()
        user = form_devis.cleaned_data['nom']
        email = form_devis.cleaned_data['email']
        service = str(form_devis.cleaned_data['service'])
        message = form_devis.cleaned_data['message']
        message_devis= ("Bonjour cher admin il y'a un utilisateur répondant au nom de " + user +  " et son email " + email +
                        "\n\n Voici sa demande : \n Service : " + service + "\n Message : " + message)

        send_mail(
            subject="Un utilisateur vient de demander un devis",
            message= message_devis,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # Assurez-vous que c'est une liste ou un tuple
        )
        return redirect('home')
