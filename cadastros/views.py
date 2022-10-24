from .models import Critico, Avaliacao
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CriticoCreate(CreateView):
    model = Critico
    listar = ["nome", "c_id"]
    template_name: str
    success_url: reverse_lazy("index")
# Create your views here.
