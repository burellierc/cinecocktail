## About

Funny project to discover Python by building a playful API with Django.

### Run project :

Create your .env file first (the file is ignored by git)

Create you virtual environment:
`python -m venv venv`

Then run the project commands:
`source venv/bin/activate`
`python -m pip install djangorestframework`
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py runserver`

### Insert values using shell :

```
from movies.models import Movie, Cocktail, Cinebar

m1 = Movie.objects.create(
    title="Brice de Nice",
    director="James Huth",
    release_year=2005,
    poster_url="https://example.com/brice.jpg",
    genre="Comédie"
)

c1 = Cocktail.objects.create(
    movie=m1,
    name="Le Brice",
    main_color="#FFFF00",
    main_ingredient="Citron",
    description="Un cocktail jaune vif à base de citron et d’ananas"
)

cb1 = Cinebar.objects.create(
    movie=m1,
    name="Bar Jaune",
    slogan="Un cocktail jaune vif !",
    drink_of_the_day="Citron Spritz",
    happy_hour_start="16:00",
    happy_hour_end="18:00",
    is_open=True
)
```