from rest_framework import generics
from .models import Game 
from .serializers import ThingSerializer


# Create your views here.

# ListAPIView
class GamesList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = ThingSerializer

# RetrieveAPIView RetrieveUpdateAPIView
class GameDitail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = ThingSerializer