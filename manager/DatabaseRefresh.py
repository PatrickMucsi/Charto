from background_task import background
from .models import ReferenceCrypto
from .Utilities import query_site, get_price
#timedelta(minutes=5)
@background(schedule=20)
def update_cryptos():
    print("Enter update_cryptos")
    cryptos = ReferenceCrypto.objects.all()
    tickers = [crypto.ticker for crypto in cryptos]
    names = ','.join(tickers)
    info = query_site(names)
    for crypto in cryptos:
        crypto.update_price(get_price(info, crypto.ticker))
        print("Updating {} to {}".format(crypto.ticker, crypto.current_price))
        crypto.save()
    print("Completed")
