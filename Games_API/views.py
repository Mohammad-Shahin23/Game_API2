from rest_framework import generics
from .models import Game 
from .serializers import ThingSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# Create your views here.

# ListAPIView
class GamesList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsAuthenticated]

# RetrieveAPIView RetrieveUpdateAPIView
class GameDitail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = ThingSerializer
    permission_classes = [IsOwnerOrReadOnly]
