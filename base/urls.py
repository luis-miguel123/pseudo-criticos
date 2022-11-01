
from operator import concat
from django.urls import path
from base.views import ajudaView, homeView, jogosView, animesView, seriesView, filmesView, sobreView, contatoView


urlpatterns = [
    
    path('', homeView.as_view(), name = 'home'),   
    path('filmes/', filmesView.as_view(), name = 'filmes'),
    path('series/', seriesView.as_view(), name = 'series'),
    path('jogos/', jogosView.as_view(), name = 'jogos'),
    path('animes/', animesView.as_view(), name = 'animes'),
    path('sobre/', sobreView.as_view(), name = 'sobre'),
    path('contato/', contatoView.as_view(), name = 'contato'),
    path('ajuda/', ajudaView.as_view(), name = 'ajuda')
    
]