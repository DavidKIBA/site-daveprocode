from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('termes/', views.terme_page, name='termes'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('recherche_introuvable/', views.recherche_introuvable, name='recherche_introuvable'),
    path('recherche/', views.recherche, name='recherche'),
    # path('bureautique/', views.bureautique, name='bureautique'),
    # path('formation-infographie/', views.formationInfographie, name='formationInfographie'),

] 