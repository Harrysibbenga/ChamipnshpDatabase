from rest_framework import viewsets
from django.contrib.auth.models import User

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Championship, Result, Driver, Team, Session, Year, Track, Weather, RoadCondition
from .serializers import ChampionshipSerializer, UserSerializer, ResultSerializer, DriverSerializer, TeamSerializer, \
    SessionSerializer, YearSerializer, TrackSerializer, WeatherSerializer, RoadConditionSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ChampionshipViewSet(viewsets.ModelViewSet):
    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TrackViewSet(viewsets.ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class YearViewSet(viewsets.ModelViewSet):
    serializer_class = YearSerializer
    queryset = Year.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = WeatherSerializer
    queryset = Weather.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class RoadConditionViewSet(viewsets.ModelViewSet):
    serializer_class = RoadConditionSerializer
    queryset = RoadCondition.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
