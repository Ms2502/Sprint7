from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

from cuentas.models import Cliente, Prestamo


# def pedirprestamo(request,customer_id):
#     valor = request.POST.get("valor")
#     cliente = Cliente.objects.get(customer_id=customer_id)
#     print(valor)
#     Prestamo.objects.create(customer_id=customer_id, loan_total = valor)
#     return redirect("cliente-detail",customer_id)


def pedirprestamo(request,customer_id):
    # valor = request.POST.get("valor")
    # cliente = Cliente.objects.get(customer_id=customer_id)
    # print(valor)
    # Prestamo.objects.create(customer_id=customer_id, loan_total = valor)
    # context={}
    return render(request,"prestamos/prestamos.html")
