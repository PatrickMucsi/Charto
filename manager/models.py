from django.db import models
from django.contrib.auth.models import User
from .CMCAccess import CMCAccess
from django_mysql.models import ListTextField
from datetime import datetime

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_balance = models.CharField(max_length=100, default='0')
    current_time = models.CharField(max_length=30, default=datetime.now())
    previous_balances = ListTextField(base_field=models.CharField(max_length=100, default='0'))
    previous_balances_times = ListTextField(base_field=models.CharField(max_length=30, default=datetime.now()))

    def update_balance(self, new_balance):
        self.previous_balances.append(self.current_balance)
        self.previous_balances_times.append(self.current_time)
        self.current_balance = new_balance
        self.current_time = datetime.now()

    def calculate_total_invested(self):
        total_invested = 0
        for crypto in user.my_cryptos.all():
            total_invested += float(crypto.spent)
        return total_invested

class ReferenceCrypto(models.Model):
    ticker = models.CharField(max_length=8)
    current_price = models.CharField(max_length=100)
    current_time = models.CharField(max_length=30, default=datetime.now())
    previous_prices = ListTextField(base_field=models.CharField(max_length=15, default='0'))
    previous_prices_times = ListTextField(base_field=models.CharField(max_length=30, default=datetime.now()))

    def update_price(self, new_price):
        self.previous_prices.append(self.current_price)
        self.previous_prices_times.append(self.current_time)
        self.current_price = new_price
        self.current_time = datetime.now()


class Crypto(models.Model):
    reference_crypto = models.ForeignKey(ReferenceCrypto, on_delete=models.PROTECT)
    amount = models.CharField(max_length=100)
    spent = models.CharField(max_length=15)
    color = models.CharField(max_length=8)
    owner = models.ForeignKey(User, related_name='my_cryptos', on_delete=models.CASCADE)
    u_id = models.UUIDField()

    def purchase(self, amount, spent):
        self.update_amount(float(self.amount) + float(amount))
        self.update_spent(float(self.spent) + float(spent))
        self.save()

    def sell(self, amount, received):
        if float(amount) <= float(self.amount):
            self.update_amount(float(self.amount) - float(amount))
        else:
            print("not possible")
        self.save()

    def update_amount(self, new_amount):
        self.amount = new_amount

    def update_spent(self, new_spent):
        self.spent = new_spent

    def get_average(self):
        return (float(self.spent) / float(self.amount))

    def get_worth(self):
        return (float(self.amount) * float(self.reference_crypto.current_price))

    def get_gainloss(self):
        return (float(self.get_worth()) - float(self.spent))

    def get_gainloss_percentage(self):
        return (self.get_gainloss() / float(self.spent)) * 100

    def get_gainloss_color(self):
        return '#ff2f2f' if self.get_gainloss_percentage() < 0 else '#79bb32'
