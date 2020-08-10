from .CryptoHandler import CryptoHandler as crypto_handler
from .AccountHandler import AccountHandler as account_handler
from .Utilities import load_supported_cryptos
from .models import Crypto

class DashboardView():
    def __init__(self, request):
        self.cryptos = crypto_handler.sort_cryptos(request.user.my_cryptos.all())
        self.supported_cryptos = self.get_supported_cryptos()
        account_handler.update_account_balance(request.user, self.cryptos)
        self.current_balance = account_handler.get_current_balance(request.user)
        self.create_dashboard(request)

    def create_dashboard(self, request):
        self.pie_chart = crypto_handler.create_pie_chart(self.cryptos)
        self.line_graph = crypto_handler.create_line_graph('account', account_handler.get_account(request.user))

    def get_supported_cryptos(self):
        return load_supported_cryptos()

class RefreshCryptoView():
    def __init__(self, request):
        self.cryptos = crypto_handler.sort_cryptos(request.user.my_cryptos.all())
        self.update_cryptos()

    def update_cryptos(self):
        crypto_handler.update_cryptos(self.cryptos)

class EditCryptoView():
    def __init__(self, uuid):
        self.crypto = Crypto.objects.get(u_id=uuid)
        self.line_graph = crypto_handler.create_line_graph('crypto', self.crypto)

class MyCryptosView():
    def __init__(self, request):
        self.account = account_handler.get_account(request.user)
        self.cryptos = crypto_handler.sort_cryptos(request.user.my_cryptos.all())
        self.total_invested = self.calculate_total_invested()

    def calculate_total_invested(self):
        total_invested = 0
        for crypto in self.cryptos:
            total_invested += float(crypto.spent)
        return total_invested

    def calculate_gainloss(self):
        return (float(self.account.current_balance) - self.calculate_total_invested())

    def calculate_gainloss_percentage(self, invested):
        return ((float(self.account.current_balance) - invested) / invested) * 100

    def get_gainloss_percentage(self):
        invested = self.calculate_total_invested()
        result = 0
        if invested > 0:
            result = self.calculate_gainloss_percentage(invested)
        return result

    def get_gainloss_color(self):
        return '#ff2f2f' if self.get_gainloss_percentage() < 0 else '#79bb32'


class UpdateCryptoView():
    def __init__(self, request, uuid):
        self.crypto = crypto_handler.get_crypto(uuid)
        self.tags = ['type','crypto_amount','transaction_amount']
        self.transact(request.POST['type'],request.POST['crypto_amount'],
        request.POST['transaction_amount'])

    def can_afford(self, sale_amount):
        return (float(self.crypto.amount) >= float(sale_amount))

    def transact(self, type, amount, money):
        if type == 'sale':
            if self.can_afford(amount):
                self.crypto.sell(amount, money)
            else:
                print("can't afford")
        elif type == 'purchase':
            self.crypto.purchase(amount, money)
        else:
            print("nope")

class ChangeColorView():
    def __init__(self, request, uuid):
        self.new_color = request.POST['color']
        self.crypto = crypto_handler.get_crypto(uuid)
        self.crypto.color = self.new_color
        self.crypto.save()

class DeleteCryptoView():
    def __init__(self, request, uuid):
        self.crypto = crypto_handler.get_crypto(uuid)
        self.response = request.POST['response'].upper()
        if self.response == 'YES':
            self.crypto.delete()
