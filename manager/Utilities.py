def load_supported_cryptos():
    f = open('manager/static/manager/cryptos.txt')
    crypto_names = f.read().split(",")
    f.close()
    return crypto_names
