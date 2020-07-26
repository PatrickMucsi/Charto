from .models import Crypto, ReferenceCrypto
from .Utilities import initial_price, query_site
from .ChartCreator import PieChart, LineGraph


class CryptoHandler():
    def add_to_portfolio(ticker):
        if ReferenceCrypto.objects.filter(ticker=ticker).exists():
            ref_crypto = ReferenceCrypto.objects.get(ticker=ticker)
        else:
            initial_price(ticker)
            ref_crypto = ReferenceCrypto.objects.create(ticker=ticker, current_price=price)
        return ref_crypto

    def update_cryptos(cryptos):
        tickers = [crypto.reference_crypto.ticker for crypto in cryptos]
        names = ','.join(tickers)
        info = query_site(names)
        for crypto in cryptos:
            crypto.reference_crypto.update_price(get_price(info, crypto.reference_crypto.ticker))
            crypto.reference_crypto.save()

    def get_crypto(uuid):
        return Crypto.objects.get(u_id=uuid)

    def sort_cryptos(cryptos):
        cryptos = list(cryptos)
        return sorted(cryptos, key=lambda Crypto: Crypto.get_worth(), reverse=True)

    def create_pie_chart(cryptos):
        return PieChart(cryptos)

    def create_line_graph(type, info):
        return LineGraph(type, info)
