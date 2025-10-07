from rest_framework import serializers
from .models import Movie, Cocktail, Cinebar

class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocktail
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    cocktail = CocktailSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

class CinebarSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True) # Read details
    movie_id = serializers.PrimaryKeyRelatedField(  # for POST/PUT
        queryset=Movie.objects.all(), write_only=True, source="movie"
    )

    class Meta:
        model = Cinebar
        fields = [
            "id",
            "movie",
            "movie_id",
            "name",
            "slogan",
            "drink_of_the_day",
            "happy_hour_start",
            "happy_hour_end",
            "is_open"
        ]