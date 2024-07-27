from django.contrib import admin
from .models import Libro, Usuario, Carrito, CarritoLibro

admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(CarritoLibro)