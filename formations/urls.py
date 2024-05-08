from django.urls import path 
from . import views


urlpatterns = [
    path('', views.formation_page, name='formation'),
    path('<slug:slug>/', views.FormationDetailView.as_view(), name='formation-detail')

]