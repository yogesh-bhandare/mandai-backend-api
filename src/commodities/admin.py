from django.contrib import admin
from .models import Commodity, CommodityScrapeEvent

# Register your models here.

admin.site.register(Commodity)
admin.site.register(CommodityScrapeEvent)