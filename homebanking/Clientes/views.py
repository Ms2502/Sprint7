from http.client import HTTPResponse
from django.shortcuts import HttpResponse

from django.shortcuts import render
from cuentas.models import *
# from homebanking.login.views import login 

# Create your views here.

def index1(request):
    return render(request,"clientes/index.html")
 
def index(request):
    listado_clientes = Cliente.objects.all()[:5]
    context = dict(listado_clientes=listado_clientes)
    return render(request,"clientes/index1.html",context)

def detail(request,customer_id):
    cliente = Cliente.objects.get(customer_id=customer_id)
    context = dict(cliente=cliente)

    return render(request,"clientes/detail.html",context)
