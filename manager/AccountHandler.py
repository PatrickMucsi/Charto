from .models import Account
class AccountHandler():
    def get_account(user):
        return Account.objects.get(user=user)

    def get_current_balance(user):
        return AccountHandler.get_account(user).current_balance

    def update_account_balance(user, cryptos):
        new_balance = 0.0
        for crypto in cryptos:
            new_balance += crypto.get_worth()

        account = Account.objects.get(user=user)
        if round(new_balance, 2) != float(account.current_balance):
            account.update_balance(round(new_balance, 2))
            account.save()
