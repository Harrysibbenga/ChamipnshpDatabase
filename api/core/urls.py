from rest_framework import routers
from django.urls import path, include

from .views import ChampionshipViewSet, UserViewSet, ResultViewSet, DriverViewSet, TeamViewSet, YearViewSet, \
    SessionViewSet, TrackViewSet, RoadConditionViewSet, WeatherViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'results', ResultViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'teams', TeamViewSet)

router.register(r'championships', ChampionshipViewSet)
router.register(r'years', YearViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'tracks', TrackViewSet)
router.register(r'road_conditions', RoadConditionViewSet)
router.register(r'weather_conditions', WeatherViewSet)


urlpatterns = [
    path('', include(router.urls))
]