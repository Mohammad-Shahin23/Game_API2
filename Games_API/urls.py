from django.urls import path
from .views import GamesList, GameDitail

urlpatterns = [
    path('', GamesList.as_view(), name='Game_list'),
    path('/<int:pk>/', GameDitail.as_view(), name='Game_detail'),
]