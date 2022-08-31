from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"login/index.html") #vendria a ser como la "landing page"

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is  None:
            return render(request, "login/login.html")
        else:
            login(request,user)
            return redirect("clientes-index")
    else:
        return render(
            request, 
            "login/login.html",
            context=dict(error="Usuario o contraseña invalidos")
            )


def logout_view(request):
    logout(request)
    return redirect("login")