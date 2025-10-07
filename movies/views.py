from rest_framework import viewsets
from .models import Movie, Cocktail, Cinebar
from .serializers import MovieSerializer, CocktailSerializer, CinebarSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class CocktailViewSet(viewsets.ModelViewSet):
    queryset = Cocktail.objects.all()
    serializer_class = CocktailSerializer

class CinebarViewSet(viewsets.ModelViewSet):
    queryset = Cinebar.objects.all()
    serializer_class = CinebarSerializer
