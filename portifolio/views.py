from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Bedroom, Team

# Create your views here.



class IndexView(ListView):
    template_name = "bedrooms/index.html"
    context_object_name = 'Bedroom'

    def get_queryset(self):
        return Bedroom.objects.all()[:4]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['Team'] = Team.objects.order_by('name')
        return context

class BedroomsView(ListView):
    model = Bedroom
    template_name = "bedrooms/bedrooms.html"
    paginate_by = 4

class BedroomDetail(DetailView):
    model = Bedroom
    context_object_name = 'Bedroom'
    template_name = "bedrooms/bedroom.html"
