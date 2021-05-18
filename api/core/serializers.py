from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Championship, Result, Driver


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'is_staff']


class ChampionshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Championship
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'