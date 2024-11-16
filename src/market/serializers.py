from rest_framework import serializers
from .models import MarketCommodity
from commodities.models import Commodity

class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'

class MarketCommoditySerializer(serializers.ModelSerializer):
    commodity = CommoditySerializer()
    class Meta:
        model = MarketCommodity
        fields = '__all__'
