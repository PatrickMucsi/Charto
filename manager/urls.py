from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.dashboard),
    path('create_crypto', views.create_crypto, name='create_crypto'),
    path('my-cryptos', views.my_cryptos, name='my_cryptos'),
    path('refresh', views.refresh_cryptos, name='refresh_cryptos'),
    path('my-cryptos/<uuid>', views.edit_crypto, name='edit_crypto'),
    path('my-cryptos/<uuid>/update', views.update, name='update'),
    path('my-cryptos/<uuid>/change-color', views.change_color, name='change_color'),
    path('my-cryptos/<uuid>/delete', views.delete, name='delete'),
]
