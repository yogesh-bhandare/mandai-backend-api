from rest_framework import viewsets
from .models import MarketCommodity
from .serializers import MarketCommoditySerializer

class MarketCommodityViewSet(viewsets.ModelViewSet):
    queryset = MarketCommodity.objects.all()
    serializer_class = MarketCommoditySerializer

