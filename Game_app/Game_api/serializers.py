from django.db import models       
from Game_api.models import Developer
from Game_api.models import GameMaker
from rest_framework.serializers import ModelSerializer

class DeveloperSerializer(ModelSerializer):
    class Meta:
        model=Developer
        fields='__all__'

class GameMakerSerializer(ModelSerializer):
    class Meta:
        model=GameMaker
        fields='__all__'


