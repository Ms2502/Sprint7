from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

from cuentas.models import Cliente, Prestamo,Cuenta
from datetime import datetime

def indexprestamo(request,customer_id):
    cuenta = Cuenta.objects.get(customer_id=customer_id)
    prestamos= Prestamo.objects.filter(customer_id = customer_id)    
    context = dict(prestamos=prestamos,cuenta=cuenta)
    return render(request,"prestamos/prestamos.html",context)

@login_required(login_url="/login/") 
def pedirprestamo(request,customer_id):
    valor = request.POST.get("valor")
    tipoprestamo = request.POST.get("loantype")
    fechaprestamo = datetime.now().strftime("%d-%m-%Y")
    tipocliente ="x"
    cliente = Cliente.objects.get(customer_id=customer_id)
    print(valor)
    print(tipoprestamo)
    print(fechaprestamo)
    # Prestamo.objects.create(customer_id=customer_id, loan_total = valor,loan_type = tipoprestamo, loan_date = fechaprestamo)
    return redirect("indexprestamo",customer_id)


# def pedirprestamo(request,customer_id):
#     valor = request.POST.get("valor")
#     cliente = Cliente.objects.get(customer_id=customer_id)
#     # print(valor)
#     # Prestamo.objects.create(customer_id=customer_id, loan_total = valor)
#     # context={}
#     return render(request,"prestamos/prestamos.html")
