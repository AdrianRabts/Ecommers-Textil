from django.db import models

# Categoría: Toallas, Sábanas, Cortinas, etc.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Colores planos disponibles
class Color(models.Model):
    nombre = models.CharField(max_length=30)
    hex = models.CharField(max_length=7, help_text="Código HEX (ej. #ffffff)")

    def __str__(self):
        return self.nombre

# Tamaños de productos textiles
TAMANIOS = [
    ('1P', '1 Plaza'),
    ('1.5P', '1.5 Plazas'),
    ('2P', '2 Plazas'),
    ('2.5P', '2.5 Plazas'),
    ('3P', '3 Plazas'),
]

# Modelo principal de producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    tamano = models.CharField(max_length=4, choices=TAMANIOS)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    destacado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} ({self.get_tamano_display()})"
