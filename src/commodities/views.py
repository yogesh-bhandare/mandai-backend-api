from rest_framework import viewsets
from .models import Commodity
from .serializers import CommoditySerializer

class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer

