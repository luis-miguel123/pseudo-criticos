from .models import Filme, Avaliacao
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class FilmeCreate(CreateView):
    model = Filme
    fields = ["nome", "genero"]
    template_name = "conteudo/form.html"
    success_url = reverse_lazy("home")


class AvaliacaoCreate(CreateView):
    model = Avaliacao
    fields = ["titulo", "critica", 'filme']
    template_name = "conteudo/form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        self.instance.autor = self.request.user
        url = super().form_valid(form)
        return url

class filmesView(TemplateView):
    template_name= "conteudo/filmes.html"
    
class seriesView(TemplateView):
    template_name= "conteudo/series.html"
    
class jogosView(TemplateView):
    template_name= "conteudo/jogos.html"
    
class animesView(TemplateView):
    template_name= "conteudo/animes.html"
"""
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
"""