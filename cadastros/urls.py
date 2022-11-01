from django.urls import path
from django.contrib.auth import views as auth_views

from .views import CriticoCreate, AvaliacaoCreate
from .views import CriticoUpdate, AvaliacaoUpdate

urlpatterns = [
    path('cadastrar-login/', CriticoCreate.as_view(), name = 'login'),
    path("cadastrar-avaliacao/", AvaliacaoCreate.as_view(), name = 'avaliacao'),

    path("editar/critico/<int:pk>/", CriticoUpdate.as_view(), name="editar-critico"),
    path("editar/avaliacao/<int:pk>/", AvaliacaoUpdate.as_view(), name="editar-avaliacao"),
]