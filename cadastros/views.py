from .models import Critico, Avaliacao
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required

# Create your views here.
class CriticoCreate(CreateView):
    model = Critico
    fields = ["nome", "senha"]
    template_name = "cadastros/critico_form.html"
    success_url = reverse_lazy("home")

#@login_required
class AvaliacaoCreate(CreateView):

    model = Avaliacao
    fields = ["texto", "critico"]
    template_name = "cadastros/avaliacao_form.html"
    success_url = reverse_lazy("home")


class CriticoUpdate(UpdateView):
    model = Critico
    fields = ["nome", "senha"]
    template_name = "cadastros/critico_form.html"
    success_url = reverse_lazy("home")

#@login_required
class AvaliacaoUpdate(UpdateView):

    model = Avaliacao
    fields = ["texto", "critico"]
    template_name = "cadastros/avaliacao_form.html"
    success_url = reverse_lazy("home")