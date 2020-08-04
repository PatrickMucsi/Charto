from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Crypto, ReferenceCrypto
from .ViewManager import *
from .Utilities import load_supported_cryptos
from .CryptoHandler import CryptoHandler as crypto_handler
from .forms import RegisterForm
from .models import Account
import requests, json, uuid

# Main home page
def home_page(request):
    return render(request, 'manager/index.html')

def login_page(request):
    return render(request, 'manager/login.html')

def signup_page(request):
    return render(request, 'manager/signup.html')

# Log in user and redirect to dashboard
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    login(request, user)
    return redirect('/dashboard')

# Create a new user and account
def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(username, email, password)
            Account.objects.create(user=new_user)
            messages.success(request, "Your account was created successfully. You can now log in.")
            return redirect("login_page")
        else:
            return render(request, 'manager/signup.html', {'form': form})

# Log out user and redirect to home page
def logout_user(request):
    logout(request)
    return redirect('home_page')

@login_required(login_url='login_page')
def dashboard(request):
    load_amount = 25
    dashView = DashboardView(request)
    return render(request, 'manager/dashboard.html', {'cryptos':dashView.cryptos[:10], 'crypto_list':dashView.supported_cryptos,
    'names':dashView.pie_chart.names,'percentages':dashView.pie_chart.percentages,'colors':dashView.pie_chart.colors,
    'line_graph_worth':dashView.line_graph.worth[-(load_amount-1):],'dates':dashView.line_graph.dates[-(load_amount-1):],
    'current_balance':dashView.current_balance})

@login_required(login_url='login_page')
def refresh_cryptos(request):
    refreshView = RefreshCryptoView(request)
    return redirect('/dashboard')

@login_required(login_url='login_page')
def create_crypto(request):
    crypto_names = load_supported_cryptos()
    ticker = request.POST['ticker'].upper()
    if ticker in crypto_names:
        amount = request.POST['amount']
        spent = 1 if float(request.POST['spent']) <= 0 else request.POST['spent']
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
def change_color(request, uuid):
    changeView = ChangeColorView(request, uuid)
    return redirect('manager:edit_crypto', uuid)

@login_required(login_url='login_page')
def delete(request, uuid):
    deleteView = DeleteCryptoView(request, uuid)
    return redirect('manager:my_cryptos')

@login_required(login_url='login_page')
def edit_crypto(request, uuid):
    load_amount = 30
    editView = EditCryptoView(uuid)
    return render(request, 'manager/edit_crypto.html', {'crypto':editView.crypto, 'line_graph_worth':editView.line_graph.worth[-(load_amount-1):],
    'dates':editView.line_graph.dates[-(load_amount-1):]})
