from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarketCommodityViewSet

router = DefaultRouter()
router.register(r'l1', MarketCommodityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
