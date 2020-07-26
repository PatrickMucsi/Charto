import requests
import json

def load_supported_cryptos():
    f = open('manager/static/manager/cryptos.txt')
    crypto_names = f.read().split(",")
    f.close()
    return crypto_names

def query_site(cryptos):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}&CMC_PRO_API_KEY=3f2deba6-cbf5-4d3b-8766-40223c806f7e'
    request = requests.get(url.format(cryptos))
    if request.json()['status']['error_code'] != 400:
        result = request.json()['data']
    else:
        result = {}

def initial_price(crypto):
    json = query_site(crypto)
    return get_price(json, crypto)

def get_price(json_prices, crypto):
    return json_prices[crypto.upper()]['quote']['USD']['price']
