
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name= "home.html"
    

class loginView(TemplateView):
    template_name= "login.html"