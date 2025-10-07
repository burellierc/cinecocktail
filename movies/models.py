from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.PositiveIntegerField()
    poster_url = models.URLField(blank=True, null=True)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Cocktail(models.Model):
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE, related_name="cocktail")
    name = models.CharField(max_length=100)
    main_color = models.CharField(max_length=7, help_text="Code hex couleur ex: #FFFF00")
    main_ingredient = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} (pour {self.movie.title})"

class Cinebar(models.Model):
    movie = models.ForeignKey(
        "Movie",
        on_delete=models.CASCADE,
        related_name="cinebars",
        help_text="Film associé à ce coin bar"
    )
    name = models.CharField(max_length=100, help_text="Nom du coin CinéBar")
    slogan = models.CharField(max_length=150, blank=True, help_text="Petit slogan amusant")
    drink_of_the_day = models.CharField(
        max_length=100,
        blank=True,
        help_text="Boisson du moment (ex: Mojito, Margarita)"
    )
    happy_hour_start = models.TimeField(blank=True, null=True)
    happy_hour_end = models.TimeField(blank=True, null=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} – {self.movie.title}"
