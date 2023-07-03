from rest_framework import serializers
from .models import Game

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Game
        fields = ('id', 'owner', 'name', 'desc', 'created_at', 'updated_at') 