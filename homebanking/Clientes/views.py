from django.shortcuts import render
from cuentas.models import *
# from homebanking.login.views import login 

# Create your views here.

def index(request):
    return render(request,"clientes/index.html")

