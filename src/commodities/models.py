from django.db import models

class Commodity(models.Model):
    code_no = models.CharField(max_length=120, unique=True, db_index=True)
    url = models.URLField(blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    commodity = models.CharField(max_length=220, blank=True, null=True)
    quantity = models.CharField(max_length=120, blank=True, null=True)
    income = models.IntegerField(blank=True, null=True, default=0)
    min_price = models.IntegerField(blank=True, null=True, default=0)
    max_price = models.IntegerField(blank=True, null=True, default=0)
    avg_price = models.IntegerField(blank=True, null=True, default=0)
    min_price_per_kg = models.IntegerField(blank=True, null=True, default=0)
    max_price_per_kg = models.IntegerField(blank=True, null=True, default=0)
    avg_price_per_kg = models.IntegerField(blank=True, null=True, default=0)
    timestamp =  models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    metadata = models.JSONField(null=True, blank=True)
    active = models.BooleanField(default=True, help_text="Scrape daily?")



class CommodityScrapeEventManager(models.Manager):
    def create_scrape_event(self, table_data, url=None):
        events = [] 
        for row_data in table_data:
            code_no = row_data.get('code_no') or None
            income = row_data.get('income')
            min_price = row_data.get('min_price') # minimum price per quintal
            max_price = row_data.get('max_price') # maximum price per quintal
            if code_no is None or income is None or min_price is None or max_price is None:
                continue
            avg_price = (min_price + max_price)//2 # avg price per quintal
            min_price_per_kg = (min_price // 100)
            max_price_per_kg = (max_price // 100)
            avg_price_per_kg = (avg_price // 100)
            commodity_, _ = Commodity.objects.update_or_create(
                code_no=code_no,
                defaults={
                    "url": url,
                    "commodity": row_data.get('commodity') or "",
                    "quantity": row_data.get('quantity') or "",
                    "income": income or 0,
                    "min_price": min_price or 0,
                    "max_price": max_price or 0,
                    "avg_price": avg_price or 0,
                    "min_price_per_kg": min_price_per_kg or 0,
                    "max_price_per_kg": max_price_per_kg or 0,
                    "avg_price_per_kg": avg_price_per_kg or 0,
                    "metadata": row_data,
                }
            )
            event = self.create(
                commodity=commodity_,
                url=url,
                code_no=code_no,
                data=row_data,
            )
            events.append(event)  
        
        return events  



class CommodityScrapeEvent(models.Model):
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE, related_name='scrape_events')
    url = models.URLField(blank=True, null=True)
    data = models.JSONField(null=True, blank=True)
    code_no = models.CharField(max_length=120, null=True, blank=True)
    
    objects = CommodityScrapeEventManager()
