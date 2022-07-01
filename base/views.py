
from operator import index
from turtle import home
from django.views.generic import TemplateView


class homeView(TemplateView):
    template_name: "home.html"