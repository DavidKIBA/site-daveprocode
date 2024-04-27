from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib import messages
from commentaires.forms import CommentairesForm
from contacts.views import news_letter_view
from devis.forms import DevisForm
from devis.views import devis_view



def home(request):
    commentaires_form = CommentairesForm()
    form_devis = DevisForm()

    if request.method == 'POST':
        # verification si l'email de l'utilisateur de la news letter est correcte et sauvegarde dans la base de données
        if 'btn_news_letter' in request.POST:
            news_letter_view(request)
        
        if 'btn_devis' in request.POST:
            devis_view(request)

        if 'btn_send_commentaire' in request.POST:
                commentaires_form = CommentairesForm(request.POST)
                if commentaires_form.is_valid():
                    commentaires_form.save()
                    return redirect('/')
    context={'commentaires_form': commentaires_form, 'devis_form': form_devis, 'title': 'Acceuil'}
    return render(request, 'home/index.html', context)


def about_page(request):
    if request.method == 'POST':
        if 'btn_news_letter' in request.POST:
            news_letter_view(request)
    context = {'title': 'A propos'}
    return render(request, 'other_page/about.html', context)


def formation_page(request):
    context = {'title': 'Formation'}
    return render(request, 'other_page/formation.html', context)

def service_page(request):
    context = {'title': 'Service'}
    return render(request, 'other_page/services.html', context)

def handle404(request, exception):
    context = {'title': 'Page introuvable'}
    return render(request, 'other_page/404.html', context)


