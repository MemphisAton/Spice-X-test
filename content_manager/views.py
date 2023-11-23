from rest_framework import viewsets

from .models import Advantage, MenuItem
from .serializers import AdvantageSerializer, MenuItemSerializer


class AdvantageViewSet(viewsets.ModelViewSet):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
