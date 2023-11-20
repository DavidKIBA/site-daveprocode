from django.shortcuts import render
from utilisateurs.models import NewsLetters
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        if 'btn_news_letter' in request.POST:
            email = request.POST['email_news_letter']
            try:
                validate_email(email)
                # L'email est valide, vous pouvez l'ajouter à la base de données
                NewsLetters.objects.create(email_news_letter=email)
            except ValidationError:
                # L'email n'est pas valide, faites quelque chose en conséquence
                ValidationError("veuillez saisir un email valide cool")
                # pass
                # message = messages.error(request, "votre mail n'est pas valide")
    return render(request, 'home/index.html')