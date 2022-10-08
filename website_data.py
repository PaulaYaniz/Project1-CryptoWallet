# from bs4 import BeautifulSoup
# https://stackoverflow.com/questions/65864645/how-to-use-binance-api-simple-get-price-by-ticker
# https://algotrading101.com/learn/binance-python-api-guide/
import requests


def WebsiteDataXLM():
    data = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=XLMEUR').json()
    xlm_price = data["price"]
    return xlm_price

'''
def WebsiteData():
    data = requests.get('https://production.api.coindesk.com/v1/currency/ticker?currencies=XLM').json()
    p_value = data['data']['currency']['XLM']['quotes']['USD']['price']
    print(p_value)

    timest = data['timestamp']
    print(timest)
'''

def WebsiteDataJPYEUR():
    data = requests.get('https://www.floatrates.com/daily/eur.json').json()
    jpy_eur = data['jpy']['rate']
    return jpy_eur
