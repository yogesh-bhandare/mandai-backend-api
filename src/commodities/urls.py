from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommodityViewSet

router = DefaultRouter()
router.register(r'commodities', CommodityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
