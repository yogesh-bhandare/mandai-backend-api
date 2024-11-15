from django.apps import apps
from celery import shared_task
import helpers


@shared_task
def scrape_commodity_url_task(url):
    if url is None:
        return 
    elif url == "":
        return
    CommodityScrapeEvent = apps.get_model('commodities', 'CommodityScrapeEvent')
    # scrape home page and get todays price rate url
    html = helpers.scrape(url)

    # get the link for the next page
    link_url = helpers.extract_link(url, html)

    # scrape main rates page
    commodityHTML = helpers.scrape(link_url)

    # get extracted table data
    data = helpers.extract_table_data(commodityHTML)
    
    # Saving scraped data in db
    CommodityScrapeEvent.objects.create_scrape_event(data, url=url)
    return


@shared_task
def scrape_commodities_task():
    Commodity = apps.get_model('commodities', 'Commodity')
    qs = Commodity.objects.filter(active=True)
    for obj in qs:
        url = obj.url
        scrape_commodity_url_task.delay(url)

