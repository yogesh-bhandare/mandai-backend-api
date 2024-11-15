from bs4 import BeautifulSoup
import requests

def extract_link(url, html):
    soup = BeautifulSoup(html, 'html.parser')
    h3_tag = soup.find('h3')
    if h3_tag:
        next_link = h3_tag.find_next('a')
        
        if next_link and 'href' in next_link.attrs:
            link_url = next_link['href']
            if not link_url.startswith('http'):
                link_url = requests.compat.urljoin(url, link_url)
    return link_url

def extract_table_data(commodityHTML):
    soup = BeautifulSoup(commodityHTML, 'html.parser')

    tables = soup.find_all('table')
    
    table_data = []
    for index, table in enumerate(tables):
        
        
        rows = table.find_all('tr')
        
        for row in rows[1:]:
            cells = row.find_all('td')
            
            if len(cells) >= 6:
                try:
                    code_no = int(cells[0].text.strip()) 
                except ValueError:
                    code_no = None 
                
                commodity = cells[1].text.strip()
                quantity = cells[2].text.strip()
                
                try:
                    income = int(cells[3].text.strip()) 
                except ValueError:
                    income = None 
                
                try:
                    min_price = int(cells[4].text.strip().replace('Rs.', '').replace('/-', '').replace(',', '').strip())
                except ValueError:
                    min_price = None 

                try:
                    max_price = int(cells[5].text.strip().replace('Rs.', '').replace('/-', '').replace(',', '').strip())
                except ValueError:
                    max_price = None 
                
                row_data = {
                            "code_no":code_no, 
                            "commodity":commodity, 
                            "quantity":quantity, 
                            "income":income, 
                            "min_price":min_price, 
                            "max_price":max_price
                            }
                table_data.append(row_data)

        # for row_data in table_data:
        #     print(row_data)

    return table_data