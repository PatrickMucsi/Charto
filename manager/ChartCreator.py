from .models import Crypto, Account
from datetime import datetime, timedelta

class PieChart():
    def __init__(self, user_cryptos):
        self.cryptos = user_cryptos
        self.names = []
        self.colors = []
        self.worth = 0
        self.percentages = []
        self.populate_lists()

    def populate_lists(self):
        for crypto in self.cryptos:
            self.names.append(crypto.reference_crypto.ticker)
            self.colors.append(crypto.color)
            self.worth += crypto.get_worth()
        self.calculate_percentages()

    def calculate_percentages(self):
        for crypto in self.cryptos:
            self.percentages.append(round((crypto.get_worth() / self.worth) * 100, 2))


class LineGraph():
    def __init__(self, type, info):
        self.dates = []
        if type == 'account':
            for balance_time in info.previous_balances_times:
                converted_balance_time = datetime.strptime(balance_time, "%Y-%m-%d %H:%M:%S.%f")
                converted_balance_time -= timedelta(hours=7)
                self.dates.append(converted_balance_time.strftime("%a-%-I:%M"))
            converted_balance_time = datetime.strptime(info.current_time, "%Y-%m-%d %H:%M:%S.%f")
            converted_balance_time -= timedelta(hours=7)
            self.dates.append(converted_balance_time.strftime("%a-%-I:%M"))
            self.worth = info.previous_balances
            self.worth.append(info.current_balance)
        elif type == 'crypto':
            for price_time in info.reference_crypto.previous_prices_times:
                converted_balance_time = datetime.strptime(price_time, "%Y-%m-%d %H:%M:%S.%f")
                converted_balance_time -= timedelta(hours=7)
                self.dates.append(converted_balance_time.strftime("%a-%-I:%M"))
            converted_balance_time = datetime.strptime(info.reference_crypto.current_time, "%Y-%m-%d %H:%M:%S.%f")
            converted_balance_time -= timedelta(hours=7)
            self.dates.append(converted_balance_time.strftime("%a-%-I:%M"))
            self.worth = info.reference_crypto.previous_prices
            self.worth.append(info.reference_crypto.current_price)
