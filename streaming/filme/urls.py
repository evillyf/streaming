from django.urls import path, include
from .views import HomeFilmes, HomePage, DetalhesFilme



urlpatterns = [
    path('', HomePage.as_view()),
    path('filmes/', HomeFilmes.as_view()),
    path('filmes/<int:pk>', DetalhesFilme.as_view())
]



