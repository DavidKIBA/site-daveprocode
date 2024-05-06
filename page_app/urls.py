from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    # path('contact/', views.contact_page, name='contact'),
    path('formation/', views.formation_page, name='formation'),
    path('service/', views.service_page, name='service'),
    path('termes/', views.terme_page, name='termes'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('service-site-web/', views.servicesiteweb, name='servicesiteweb'),
    path('service-graphisme/', views.servicegraphisme, name='servicegraphisme'),
    path('service-strategie-numerique/', views.servicestrategienumerique, name='servicestrategienumerique'),
    path('service-software/', views.servicesoftware, name='servicesoftware'),
    path('formation-site-web/', views.formationsiteweb, name='formationsiteweb'),

] 