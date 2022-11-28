from django.urls import path


from .views import FilmeCreate, AvaliacaoCreate

urlpatterns = [
    path('cadastrar-filme', FilmeCreate.as_view(), name = 'filme'),
    path("cadastrar-avaliacao", AvaliacaoCreate.as_view(), name = 'avaliacao'),
]

'''
    path('filmes/', filmesView.as_view(), name = 'filmes'),
    path('series/', seriesView.as_view(), name = 'series'),
    path('jogos/', jogosView.as_view(), name = 'jogos'),
    path('animes/', animesView.as_view(), name = 'animes'),
'''