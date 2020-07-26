from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Crypto, ReferenceCrypto
from .ViewManager import DashboardView, EditCryptoView, UpdateCryptoView, DeleteCryptoView, MyCryptosView
from .Utilities import load_supported_cryptos
from .CryptoHandler import CryptoHandler as crypto_handler
import requests, json, uuid

@login_required(login_url='login_page')
def dashboard(request):
    dashView = DashboardView(request)
    return render(request, 'manager/dashboard.html', {'cryptos':dashView.cryptos[:10], 'crypto_list':dashView.supported_cryptos,
    'names':dashView.pie_chart.names,'percentages':dashView.pie_chart.percentages,'colors':dashView.pie_chart.colors, 'line_graph_worth':dashView.line_graph.worth[-19:],
    'dates':dashView.line_graph.dates[-19:], 'current_balance':dashView.current_balance})

def login_page(request):
    return render(request, 'manager/index.html', {})

@login_required(login_url='login_page')
def create_crypto(request):
    crypto_names = load_supported_cryptos()
    ticker = request.POST['ticker'].upper()
    if ticker in crypto_names:
        amount = request.POST['amount']
        spent = request.POST['spent']
        color = request.POST['color']
        ref_crypto = crypto_handler.add_to_portfolio(ticker)
        crypto = Crypto.objects.create(reference_crypto=ref_crypto, amount=amount, spent=spent, color=color, owner=request.user, u_id=uuid.uuid4())
        return redirect('/dashboard')
    else:
        print("crypto not supported")

@login_required(login_url='login_page')
def my_cryptos(request):
    cryptoView = MyCryptosView(request)
    return render(request, 'manager/my_cryptos.html', {'cryptos':cryptoView.cryptos, 'user':cryptoView.account, 'info':cryptoView})

@login_required(login_url='login_page')
def update(request, uuid):
    updateView = UpdateCryptoView(request, uuid)
    return redirect('manager:edit_crypto', uuid)

@login_required(login_url='login_page')
def delete(request, uuid):
    deleteView = DeleteCryptoView(request, uuid)
    return redirect('manager:my_cryptos')

@login_required(login_url='login_page')
def edit_crypto(request, uuid):
    editView = EditCryptoView(uuid)
    return render(request, 'manager/edit_crypto.html', {'crypto':editView.crypto, 'line_graph_worth':editView.line_graph.worth[-14:],
    'dates':editView.line_graph.dates[-14:]})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return redirect('/dashboard')

def logout_user(request):
    logout(request)
    return redirect('login_page')
