
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name= "home.html"
    

class loginView(TemplateView):
    template_name= "login.html"
    
class filmesView(TemplateView):
    template_name= "filmes.html"
    
class seriesView(TemplateView):
    template_name= "series.html"
    
class jogosView(TemplateView):
    template_name= "jogos.html"
    
class animesView(TemplateView):
    template_name= "animes.html"
    
class sobreView(TemplateView):
    template_name= 'sobre.html'
    
class contatoView(TemplateView):
    template_name= 'contato.html'
    
class ajudaView(TemplateView):
    template_name= 'ajuda.html'