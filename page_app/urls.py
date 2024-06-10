from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('termes/', views.terme_page, name='termes'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('recherche/', views.search_view, name='recherche'),

] 