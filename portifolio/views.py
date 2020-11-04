from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Bedroom, Team, Image

# Create your views here.



def IndexView(request):
   

    bedrooms = Bedroom.objects.all()[:4]
    banner_img = Image.objects.get(name="slider03")
    partiners_img = Image.objects.get(name="partiners") 
    teams = Team.objects.all()
    values = {'bedrooms': bedrooms, 'banner': banner_img, 'partiners_img': partiners_img, 'teams': teams}

    return render(request, 'bedrooms/index.html', {'values': values})

class BedroomsView(ListView):
    model = Bedroom
    template_name = "bedrooms/bedrooms.html"
    paginate_by = 4

class BedroomDetail(DetailView):
    model = Bedroom
    context_object_name = 'Bedroom'
    template_name = "bedrooms/bedroom.html"
