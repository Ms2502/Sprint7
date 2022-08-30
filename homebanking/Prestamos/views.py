from django.shortcuts import render,redirect
from cuentas.models import Cliente, Prestamo

from django.http import HttpResponse


# Create your views here.

def pedirprestamo(request,customer_id):
    valor = request.POST.get("valor")
    cliente = Cliente.objects.get(customer_id=customer_id)
    print(valor)
    Prestamo.objects.create(customer_id=customer_id, loan_total = valor)
    return redirect("cliente-detail",customer_id)