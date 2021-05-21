from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for key, value in data.items():
            try:
                if not value:
                    data[key] = ""
            except KeyError:
                pass
        return data
