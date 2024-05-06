from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_page, name='service'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='detail-service'),


]