
from operator import concat
from django.urls import path, include
from base.views import ajudaView, homeView, sobreView, contatoView, modeloView


urlpatterns = [
    
    path('', homeView.as_view(), name = 'home'),
    path('modelo/', modeloView.as_view(), name = 'modelo'),
    path('sobre/', sobreView.as_view(), name = 'sobre'),
    path('contato/', contatoView.as_view(), name = 'contato'),
    path('ajuda/', ajudaView.as_view(), name = 'ajuda'),
]