from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    # path('contact/', views.contact_page, name='contact'),
    path('formation/', views.formation_page, name='formation'),
    path('termes/', views.terme_page, name='termes'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('recherche/', views.recherche, name='recherche_introuvable'),
    path('bureautique/', views.bureautique, name='bureautique'),
    path('formation-infographie/', views.formationInfographie, name='formationInfographie'),

] 