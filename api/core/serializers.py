from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Championship, Result, Driver, Team, Track, RoadCondition, Weather, Session, Year


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
        model = Track
        fields = '__all__'


class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'


class RoadConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadCondition
        fields = '__all__'

