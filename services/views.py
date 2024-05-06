from django.shortcuts import render
from .models import MiniService
from django.views.generic import DetailView

# Create your views here.

def service_page(request):

    services = MiniService.objects.all()

    context = {'title': 'Service', 'services': services}
    return render(request, 'service/services.html', context)

class ServiceDetailView(DetailView):

    model = MiniService
    context_object_name = "service"
    template_name = 'service/service-detail.html'


def servicesiteweb(request):
    context = {'title': 'servicesiteweb'}
    return render(request, 'service/servicesiteweb.html', context)

def servicegraphisme(request):
    context = {'title': 'servicegraphisme'}
    return render(request, 'service/servicegraphisme.html', context)

def servicestrategienumerique(request):
    context = {'title': 'servicestrategienumerique'}
    return render(request, 'service/servicestrategienumerique.html', context)

def servicesoftware(request):
    context = {'title': 'servicesoftware'}
    return render(request, 'service/servicesoftware.html', context)

def formationsiteweb(request):
    context = {'title': 'formationsiteweb'}
    return render(request, 'formation/formationsiteweb.html', context)

def serviceappweb(request):
    context = {'title': 'serviceappweb'}
    return render(request, 'service/serviceappweb.html', context)

def servicepub(request):
    context = {'title': 'servicepub'}
    return render(request, 'service/servicepub.html', context)

def servicehardware(request):
    context = {'title': 'servicehardware'}
    return render(request, 'service/servicehardware.html', context)

def serviceseo(request):
    context = {'title': 'serviceseo'}
    return render(request, 'service/serviceseo.html', context)

def servicesupports(request):
    context = {'title': 'servicesupports'}
    return render(request, 'service/servicesupports.html', context)