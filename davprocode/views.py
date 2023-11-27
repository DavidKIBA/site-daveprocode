from django.shortcuts import render, redirect
from utilisateurs.models import NewsLetters
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from commentaires.forms import CommentairesForm


def home(request):
    commentaires_form = CommentairesForm()

    if request.method == 'POST':
        # verification si l'email de l'utilisateur de la news letter est correcte et sauvegarde dans la base de données
        if 'btn_news_letter' in request.POST:
            email = request.POST['email_news_letter']
            try:
                validate_email(email)
                # L'email est valide, vous pouvez l'ajouter à la base de données
                NewsLetters.objects.create(email_news_letter=email)
            except ValidationError as e:
                # L'email n'est pas valide, faites quelque chose en conséquence
                messages.error(request, f"Erreur: {e}")

        if 'btn_send_commentaire' in request.POST:
                commentaires_form = CommentairesForm(request.POST)
                if commentaires_form.is_valid():
                    commentaires_form.save()
                    return redirect('/')
    context={'commentaires_form': commentaires_form}
    return render(request, 'home/index.html', context)


def about_page(request):
     return render(request, 'other_page/about.html')

