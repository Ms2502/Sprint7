from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"login/index.html")

def login(request):
    return render(request, "login/login.html")

# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect("index")

#         return render(
#             request,
#             "login/login.html",
#             context = dict(error="Usuario o contraseña incorrectos"),
#             )
#     return render(request,"login/login.html")

def logout_view(request):
    pass