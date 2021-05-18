from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .serializers import ChampionshipSerializer, UserSerializer, ResultSerializer, DriverSerializer
from .models import Championship, Result, Driver
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ChampionshipViewSet(viewsets.ModelViewSet):
    serializer_class = ChampionshipSerializer
    queryset = Championship.objects.all()


class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    queryset = Result.objects.all()

class DriverViewSet(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()