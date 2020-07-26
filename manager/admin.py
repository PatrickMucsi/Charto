from django.contrib import admin
from .models import Crypto, ReferenceCrypto, Account

admin.site.register(Crypto)
admin.site.register(ReferenceCrypto)
admin.site.register(Account)
