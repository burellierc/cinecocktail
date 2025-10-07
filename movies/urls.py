from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, CocktailViewSet, CinebarViewSet

router = DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"cocktails", CocktailViewSet)
router.register(r"cinebars", CinebarViewSet)

urlpatterns = router.urls