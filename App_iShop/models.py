from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    
    nombre = models.CharField(max_length=30)
    especificaciones = models.TextField(max_length=200)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='img/productos/', default='img/productos/default.jpg')
    
    class Meta:
        verbose_name_plural = "Productos"
    
    def __str__(self):
        return self.nombre
    
class Notebook(Producto):
    
    class Meta:
        verbose_name_plural = "Notebooks"
    
    tipo = "notebook"
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Notebooks"

class Celular(Producto):
    
    tipo = "celular"
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Celulares"

class Accesorio(Producto):
    
    tipo = "accesorio"
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Accesorios"
    
class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carrito")

    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    class Meta:
        verbose_name_plural = "Carritos"

class CarritoItem(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos")
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} de {self.usuario.username}"
    
    class Meta:
        verbose_name_plural = "Pedidos"

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio en el momento de la compra

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - Pedido #{self.pedido.id}"
    

class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avatar')
    imagen = models.ImageField(upload_to='img/avatars/', blank=True, null=True, default='img/avatars/default.jpg')
    
    def __str__(self):
        return f'Avatar de {self.usuario}'