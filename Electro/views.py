from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Electro

class AboutPageView(TemplateView):
    template_name = 'Electro/about.html'
    
class ElectroHomeView(TemplateView):
    template_name = "Electro/home.html"
    model = Electro


class ElectroListView(ListView):
    template_name = "Electro/electro_list.html"
    model = Electro


class ElectroDetailView(DetailView):
    template_name = "Electro/electro_detail.html"
    model = Electro
    context_object_name = "electro_detail"


class ElectroCreateView(CreateView):
    template_name = "Electro/electro_create.html"
    model = Electro
    fields = ["owner", "elctronic_name", "elctronic_image", "description"]


class ElectroUpdateView(UpdateView):
    template_name = "Electro/electro_update.html"
    model = Electro
    fields = ["elctronic_name", "elctronic_image", "description"]
    template_name_suffix = '_update_form'

class ElectroDeleteView(DeleteView):
    template_name = "Electro/electro_delete.html"
    model = Electro
    success_url = reverse_lazy("Electro_list")
