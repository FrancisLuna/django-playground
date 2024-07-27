from django import forms

class LibroForm(forms.Form):
    isbn = forms.CharField(max_length=13, label="ISBN")
    nombre = forms.CharField(max_length=255, label="Nombre")
    genero = forms.CharField(max_length=100, label="Género")
    autor = forms.CharField(max_length=255, label="Autor")
    precio = forms.DecimalField(max_digits=6, decimal_places=2, label="Precio")


class BuscarLibro(forms.Form):
    isbn = forms.CharField(max_length=13, label="Buscar por ISBN")



