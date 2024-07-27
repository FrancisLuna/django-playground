from django.db import models
from django.contrib.auth.models import User

# Modelo para los libros
class Libro(models.Model):
    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    genero = models.CharField(max_length=100, verbose_name="Género")
    autor = models.CharField(max_length=255, verbose_name="Autor")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio")

    def __str__(self):
        return str(self.nombre)

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"


# Modelo para los usuarios
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    direccion_envio = models.TextField(verbose_name="Dirección de envío")
    email = models.EmailField(unique=True, verbose_name="Email")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"


# Modelo para el carrito
class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carritos")
    libros = models.ManyToManyField(Libro, through='CarritoLibro')

    def __str__(self):
        return f"Carrito de {self.usuario}"

    class Meta:
        verbose_name = "Carrito"
        verbose_name_plural = "Carritos"


# Tabla intermedia para relación muchos a muchos entre Carrito y Libro
class CarritoLibro(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.libro} en {self.carrito}"

    class Meta:
        verbose_name = "CarritoLibro"
        verbose_name_plural = "CarritosLibros"
