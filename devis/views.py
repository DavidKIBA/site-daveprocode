from django.shortcuts import render, redirect
from .forms import DevisForm

# Create your views here.

def devis_view(request):
    # form_devis = DevisForm()

    form_devis = DevisForm(request.POST)
    if form_devis.is_valid():
        form_devis.save()
        return redirect('home')
