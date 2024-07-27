from django.shortcuts import render
from .models import Libro
from mi_app.forms import LibroForm, BuscarLibro

def inicio(request):
    # return render(request, "Hola")
    return render(request, "mi_app/index.html")

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, "mi_app/libro_list.html", {'libros': libros})
    # return render(request, "mi_app/libro_list.html")

def usuario_list(request):
    return render(request, "mi_app/usuario_list.html")

def carrito_list(request):
    return render(request, "mi_app/carrito_list.html")


# Formularios
def libro_create(request):
    if request.method == "POST":
        libro_form = LibroForm(request.POST)
        if libro_form.is_valid():
            libro = Libro(
                isbn=libro_form.cleaned_data['isbn'],
                nombre=libro_form.cleaned_data['nombre'],
                genero=libro_form.cleaned_data['genero'],
                autor=libro_form.cleaned_data['autor'],
                precio=libro_form.cleaned_data['precio']
            )
            libro.save()
            return render(request, "mi_app/index.html")
    else:
        libro_form = LibroForm()
    return render(request, "mi_app/libro_create.html", {"libro_create_form": libro_form})

def buscar_libro(request):
    if request.method == "POST":
        buscar_libro_form = BuscarLibro(request.POST)
        if buscar_libro_form.is_valid():
            isbn_search = buscar_libro_form.cleaned_data["isbn"]            
            libro = Libro.objects.get(isbn=isbn_search)
            return render(request, "mi_app/resultado_libro.html", {"libro": libro})
    else:
        buscar_libro_form = BuscarLibro()

    return render(request, "mi_app/buscar-libro.html", {"buscar_libro_form": buscar_libro_form})
