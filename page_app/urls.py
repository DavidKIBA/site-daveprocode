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
    path('servicesiteweb/', views.servicesiteweb, name='servicesiteweb'),
    path('servicegraphisme/', views.servicegraphisme, name='servicegraphisme'),
    path('servicestrategienumerique/', views.servicestrategienumerique, name='servicestrategienumerique'),
    path('servicesoftware/', views.servicesoftware, name='servicesoftware'),
    path('formationsiteweb/', views.formationsiteweb, name='formationsiteweb'),
    path('serviceappweb/', views.serviceappweb, name='serviceappweb'),
    path('servicepub/', views.servicepub, name='servicepub'),
    path('servicehardware/', views.servicehardware, name='servicehardware'),
    path('serviceseo/', views.serviceseo, name='serviceseo'),
    path('servicesupports/', views.servicesupports, name='servicesupports'),
    path('recherche/', views.recherche, name='recherche_introuvable'),
    path('bureautique/', views.bureautique, name='bureautique'),
    path('formationInfographie/', views.formationInfographie, name='formationInfographie'),
] 