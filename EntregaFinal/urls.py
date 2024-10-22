"""
URL configuration for EntregaFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App_iShop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contacto', contacto, name='contacto'),
    path('productos', productos, name='productos'),
    path('productos_detalle/<pk>', productos_detalle.as_view(), name='productos_detalle'),
    path('productos_editar/<pk>', productos_editar.as_view(), name='productos_editar'),
    path('productos_eliminar/<pk>', productos_eliminar.as_view(), name='productos_eliminar'),
    path('notebooks', notebooks.as_view(), name='notebooks'),
    path('agregar_notebook', agregar_notebook.as_view(), name='agregar_notebook'),
    path('celulares', celulares.as_view(), name='celulares'),
    path('agregar_celular', agregar_celular.as_view(), name='agregar_celular'),
    path('accesorios', accesorios.as_view(), name='accesorios'),
    path('agregar_accesorio', agregar_accesorio.as_view(), name='agregar_accesorio'),
    path('buscar', buscar_productos, name='buscar'),
    path('buscar_resultado', buscar_resultado, name='buscar_resultado'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('cambiar_password/', cambiar_password, name='cambiar_password'),
    path('perfil/', perfil, name='perfil'),
    path('denegado/', denegado, name='denegado'),
    path('avatar/', avatar.as_view(), name='avatar'),
    #CARRITO
    path('carrito/', CarritoView.as_view(), name='carrito'),
    path('carrito_agregar_item/<int:producto_id>/', AgregarItemView.as_view(), name='carrito_agregar_item'),
    path('eliminar_item/<int:item_id>/', EliminarItemView.as_view(), name='eliminar_item'),
    #PEDIDO
    path('pedido/', PedidoView.as_view(), name='crear_pedido'),
    path('ver_pedido/<int:pedido_id>/', PedidoDetalleView.as_view(), name='ver_pedido'),
    path('mis_pedidos/', PedidoListarView.as_view(), name='mis_pedidos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
