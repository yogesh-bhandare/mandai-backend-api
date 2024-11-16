from django.db import models
from commodities.models import Commodity

class Vendor(models.Model):
    shop_no = models.CharField(max_length=120, unique=True, db_index=True)
    vendor_name = models.CharField(max_length=220, default="")
    shop_name = models.CharField(max_length=220, blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=10, unique=True, db_index=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    commodities = models.ManyToManyField(Commodity, related_name='vendors', blank=True)
    min_qty_per_kg = models.PositiveIntegerField(default=0, blank=True)
    max_qty_per_kg = models.PositiveIntegerField(default=0, blank=True)
    verified = models.BooleanField(default=False, help_text="Is the vendor verified?")
    active = models.BooleanField(default=True, help_text="Is the vendor active?")
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)