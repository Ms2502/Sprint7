from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('', views.pedirprestamo, name='pedirprestamo'),
    path('<int:customer_id>/', views.pedirprestamo, name='prestamos-pedirprestamo'),

    ]