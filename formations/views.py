from django.shortcuts import render
from .models import Formations
from django.views.generic import DetailView

# Create your views here.

def formation_page(request):
    formations = Formations.objects.all()
    context = {'title': 'Formation', 'formations': formations}
    return render(request, 'formation/formatio.html', context)


class FormationDetailView(DetailView):

    model = Formations
    context_object_name = "formation"
    template_name = "formation/formation-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        formation = self.get_object()
        context['title'] = formation.titre
        return context