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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = self.get_object()
        context['title'] = service.titre
        return context
