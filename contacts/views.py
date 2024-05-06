from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from .models import NewsLetters
from .forms import ContactForm
from django.contrib import messages
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def contact_page(request):
    message = ""
    contact_form = ContactForm()
    if request.method == 'POST':
        if 'btn_news_letter' in request.POST:
            news_letter_view(request)
            
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            send_mail(
                subject="Vous avez un message de la partie contact",
                message="Un utilisateur vient de laisser un message sur la page contact",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # Assurez-vous que c'est une liste ou un tuple
                fail_silently=False
            )

            message = messages.success(request, 'votre message a été envyer avec succes nous allons vous répondre pas mail dans maximum 2 jours')
            return redirect('contact')
     
    context ={'contact_form': contact_form, 'message': message, 'title': 'Contact'}
    return render(request, 'other_page/contact.html', context)

def news_letter_view(request):

    email = request.POST['email_news_letter']
    try:
        validate_email(email)
        # L'email est valide, vous pouvez l'ajouter à la base de données
        NewsLetters.objects.create(email_news_letter=email)
    except ValidationError as e:
        # L'email n'est pas valide, faites quelque chose en conséquence
        messages.error(request, f"Erreur: {e}")
    
    # return render(request, 'base/footer.html')
