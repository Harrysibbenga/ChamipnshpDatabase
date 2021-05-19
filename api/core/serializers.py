from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Championship, Result, Driver, Team, Track


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
        fields = ['id', 'first_name', 'last_name', 'dob', 'nat', 'image', 'podiums']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        modal = Track
        fields = '__all__'
