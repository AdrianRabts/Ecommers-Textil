from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('producto/<int:pk>/', views.detalle_producto, name='detalle_producto'),
]
