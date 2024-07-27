from django.urls import path
from mi_app import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('libros/', views.libro_list, name="Libros"),
    path('usuarios/', views.usuario_list, name='Usuario'),
    path('carritos/', views.carrito_list, name='Carrito'),
]

formularios = [
    path('libro-create/', views.libro_create, name="Añadir_Libro"),
    path('buscar-libro/', views.buscar_libro, name="Buscar-Libro"),
]

urlpatterns += formularios