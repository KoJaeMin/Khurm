from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import File, Shared


class FileSerializer(serializers.ModelSerializer):
    auth_username = ReadOnlyField(source='author.username')
    file = serializers.FileField(use_url = True)

    class Meta:
        model = File
        fields = '__all__'

class SharedSerializer(serializers.ModelSerializer):
    user_no = serializers.IntegerField(source='user_no.id', read_only=True)
    file_no = serializers.IntegerField(source='file_no.f_no', read_only=True)

    class Meta:
        model = Shared
        fields = '__all__'