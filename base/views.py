
from operator import index
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name: "index.html"