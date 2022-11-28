
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name= "base/index.html"

class modeloView(TemplateView):
    template_name = 'base/modelo.html'
    
class sobreView(TemplateView):
    template_name= 'base/sobre.html'
    
class contatoView(TemplateView):
    template_name= 'base/contato.html'
    
class ajudaView(TemplateView):
    template_name= 'base/ajuda.html'