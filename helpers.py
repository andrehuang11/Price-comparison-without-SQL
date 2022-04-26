import requests
from bs4 import BeautifulSoup

def get_price(product_url):
    session = requests.Session()
    page = session.get(url=product_url)
    soup = BeautifulSoup(page.content,'lxml')
    if "sonda" in product_url:
        tag = soup.find('span', class_ = 'price')
        try:
            price = tag.text.strip()
        except:
            price = "Indisponível"
    else:
        tag = soup.find('div', class_ = 'current-pricesectionstyles__CurrentPrice-sc-17j9p6i-0 drikI')
        if "clubeextra" in product_url:
            try:
                price = tag.text.strip()
            except:
                price = "Indisponível"
        else:
            try:
                price = tag.text.strip()
            except:
                price = "Indisponível"
    return price

def create_dictionary(url, price, dictionary):
    if "sonda" in url:
        dictionary["Sonda"] = price
    elif "clubeextra" in url:
        dictionary["Extra"] = price
    else:
        dictionary["Pão de açúcar"] = price


