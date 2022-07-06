
from operator import concat
from django.urls import path
from base.views import ajudaView, homeView, jogosView, animesView, loginView, seriesView, filmesView, sobreView, contatoView


urlpatterns = [
    
    path('home/', homeView.as_view()),
    path('login/', loginView.as_view()),
    path('filmes/', filmesView.as_view()),
    path('series/', seriesView.as_view()),
    path('jogos/', jogosView.as_view()),
    path('animes/', animesView.as_view()),
    path('sobre/', sobreView.as_view()),
    path('contato/', contatoView.as_view()),
    path('ajuda/', ajudaView.as_view())
    
]