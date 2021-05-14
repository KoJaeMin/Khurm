from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import File


class FileSerializer(serializers.ModelSerializer):
    #auth_username = ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url = True)

    class Meta:
        model = File
        fields = '__all__'
