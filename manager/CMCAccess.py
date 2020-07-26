import requests
import json

class CMCAccess():
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={}&CMC_PRO_API_KEY=3f2deba6-cbf5-4d3b-8766-40223c806f7e'

    def query_site(self, cryptos):
        request = requests.get(self.url.format(cryptos))
        if request.json()['status']['error_code'] != 400:
            return request.json()['data']
        else:
            print("shit")

    def initial_price(self, crypto):
        json = self.query_site(crypto)
        return self.get_price(json, crypto)

    def get_price(self, json, crypto):
        return json[crypto.upper()]['quote']['USD']['price']
