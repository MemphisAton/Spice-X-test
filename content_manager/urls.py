from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdvantageViewSet, MenuItemViewSet

router = DefaultRouter()
router.register(r'advantages', AdvantageViewSet, basename='advantage')
router.register(r'menuitems', MenuItemViewSet, basename='menuitem')

urlpatterns = [
    path('', include(router.urls)),
]