from django.db import models
from commodities.models import Commodity

# Create your models here.
class MarketCommodity(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='market_commodities')
    quantity_kg = models.IntegerField(default=0)
    expected_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
