import requests
import json

def load_supported_cryptos():
    f = open('manager/static/manager/cryptos.txt')
    crypto_names = f.read().split(",")
    f.close()
    return crypto_names

def query_site(cryptos):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}&CMC_PRO_API_KEY=APIKEYHERE'
    request = requests.get(url.format(cryptos))
    if request.json()['status']['error_code'] != 400:
        result = request.json()['data']
    else:
        result = {}
    return result

def initial_price(crypto):
    json_info = query_site(crypto)
    return get_price(json_info, crypto)

def get_price(json_prices, crypto):
    return json_prices[crypto.upper()]['quote']['USD']['price']
