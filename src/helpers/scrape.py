from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

options = ChromeOptions()

def scrape(url=None, body_only=True):
    print("Connecting to the scraping browser...")
    html = ""
    with webdriver.Chrome(options=options) as driver:
        print(f"Connected Navigating to {url}")
        driver.get(url)
        print("Navigated! Scraping page content.")
        html = driver.page_source
        if body_only:
            body = driver.find_element(By.TAG_NAME, "body")
            html = body.get_attribute('innerHTML')
    return html
