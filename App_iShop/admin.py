from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Producto)
admin.site.register(Notebook)
admin.site.register(Celular)
admin.site.register(Accesorio)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(Avatar)
