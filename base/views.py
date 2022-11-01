
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name= "base/index.html"

class filmesView(TemplateView):
    template_name= "base/filmes.html"
    
class seriesView(TemplateView):
    template_name= "base/series.html"
    
class jogosView(TemplateView):
    template_name= "base/jogos.html"
    
class animesView(TemplateView):
    template_name= "base/animes.html"
    
class sobreView(TemplateView):
    template_name= 'base/sobre.html'
    
class contatoView(TemplateView):
    template_name= 'base/contato.html'
    
class ajudaView(TemplateView):
    template_name= 'base/ajuda.html'