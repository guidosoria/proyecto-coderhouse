#Para renderizar plantillas en Django y hacer redirecciones
from django.shortcuts import render, redirect, get_object_or_404

#Importo mis formularios de Django
from .forms import *

#Para el CRUD (Create, Read, Update, Delete)
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View

#Para la vista en detalle de un producto
from django.views.generic.detail import DetailView

#Para el inicio de sesión, registro y modificación de usuarios
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.views import LogoutView

#Para forzar el inicio de sesión al utilizar la view - Para views basadas en Funciones
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

#Para validar que es un superadmin en algunas views
def superadmin(user):
    return user.is_superuser


# #INDEX CON AVATAR
# def index(req):

#     #Valido si el usuario tiene un avatar asociado
#     try:    
#         avatar = Avatar.objects.get(usuario=req.user.id)
#         return render(req, "index.html", {'mensaje':'index', 'url': avatar.imagen.url})
    
#     except:
#         return render(req, "index.html", {'mensaje':'index', 'url': '/media/img/avatars/default.jpg'})

def index(req):

    return render(req, 'index.html', {'mensaje': 'index'})

def about(req):
    
    return render(req, "about.html", {})

def contacto(req):
    
    return render(req, "contacto.html", {})

def productos(req):
    
    return render(req, "productos.html", {})

class productos_detalle(DetailView):
    
    model = Producto
    template_name = 'detalle.html'
    context_object_name = 'producto'
    
class productos_editar(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = Producto
    template_name = "productos_editar.html"
    fields = ('__all__')
    success_url = '/'
    context_object_name = 'producto'
    
    def test_func(self):
    # Retorna True si el usuario es superadmin
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
    # Redirigir a una página específica si no pasa el test
        return redirect('denegado')

class productos_eliminar(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = Producto
    template_name = 'productos_eliminar.html'
    context_object_name = 'producto'
    success_url = '/productos'
    
    def test_func(self):
    # Retorna True si el usuario es superadmin
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
    # Redirigir a una página específica si no pasa el test
        return redirect('denegado')

class notebooks(ListView):
    
    model = Notebook
    template_name = 'productos_notebooks.html'
    context_object_name = 'productos'
    
class celulares(ListView):
    
    model = Celular
    template_name = 'productos_celulares.html'
    context_object_name = 'productos'
    
class accesorios(ListView):
    
    model = Accesorio
    template_name = 'productos_accesorios.html'
    context_object_name = 'productos'
    

class agregar_notebook(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    model = Notebook
    template_name = "productos_agregar_notebook.html"
    fields = ['nombre', 'especificaciones', 'precio', 'imagen']
    success_url = '/notebooks'
    
    def test_func(self):
        # Retorna True si el usuario es superadmin
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
    # Redirigir a una página específica si no pasa el test
        return redirect('denegado')

class agregar_celular(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    model = Celular
    template_name = "productos_agregar_celular.html"
    fields = ['nombre', 'especificaciones', 'precio', 'imagen']
    success_url = '/celulares'
    
    def test_func(self):
        # Retorna True si el usuario es superadmin
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
    # Redirigir a una página específica si no pasa el test
        return redirect('denegado')

class agregar_accesorio(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    model = Accesorio
    template_name = "productos_agregar_accesorio.html"
    fields = ['nombre', 'especificaciones', 'precio', 'imagen']
    success_url = '/accesorios'
    
    def test_func(self):
        # Retorna True si el usuario es superadmin
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        # Redirigir a una página específica si no pasa el test
        return redirect('denegado')

def buscar_productos(req):
    
    formulario = BusquedaForm()
    
    return render(req, "busqueda.html", {"formulario": formulario})

def buscar_resultado(req):
    
    if req.GET["nombre"]:
        
        formulario = BusquedaForm(req.GET)
        
        if formulario.is_valid():
            
            nombre = formulario.cleaned_data["nombre"]
            productos = Producto.objects.filter(nombre__icontains=nombre)
            
            if len(productos) == 0:
                
                return render(req, "productos_busqueda_fallida.html", {})
                
            else:
                
                return render(req, "productos_busqueda_resultado.html", {"productos":productos})
            
def login_view(req):
    
    if req.method == "POST":
        
        formulario = AuthenticationForm(req, data=req.POST)
        if formulario.is_valid():
            
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
        
            user = authenticate(username=username, password=password)
            
            if user:
                login(req, user)
                return render(req, 'index.html', {'mensaje':f'¡Bienvenido {user.username} a iShop!'})
            else:
                return render(req, 'index.html', {'mensaje':'Failed to login. Please check your username and password.'})
        else:
            return render(req, 'login.html', {'form': formulario})
            
    else:
        
        formulario = AuthenticationForm()
        
        return render(req, 'login.html', {'form': formulario})
    
class logout_view(LogoutView):
    
    template_name = 'logout.html'
    
    
def registro(req):

    if req.method == 'POST':
        
        formulario = UserCreationForm(req.POST)
        
        if formulario.is_valid():
            
            username = formulario.cleaned_data['username']
            
            formulario.save()
            
            return render(req, 'index.html', {'mensaje':f'Registro de usuario {username} exitoso. Ahora puedes iniciar sesión.'})
            
        else:
            
            return render(req, 'registro.html', {'formulario': formulario})
        
    else:
        
        formulario = UserCreationForm()
        
        return render(req, 'registro.html', {'formulario': formulario})
    
@login_required()
def editar_perfil(req):
    
    usuario = req.user
    
    if req.method == 'POST':
        
        formulario = FormularioEditarPerfil(req.POST)
        
        if formulario.is_valid():
            
            data = formulario.cleaned_data
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.save()
            
            return render(req, 'index.html', {'mensaje':f'El cambio en tu información ha sido guardado exitosamente.'})
            
        else:
            
            return render(req, 'editar_perfil.html', {'formulario': formulario})
        
    else:
        
        formulario = FormularioEditarPerfil(instance=req.user)
        
        return render(req, 'editar_perfil.html', {'formulario': formulario})

@login_required()
def cambiar_password(req):
    
    if req.method == 'POST':
        
        formulario = PasswordChangeForm(user=req.user, data=req.POST)
        
        if formulario.is_valid():
            
            formulario.save()
            
            update_session_auth_hash(req, formulario.user)
            
            return render(req, 'index.html', {'mensaje':f'El cambio de contraseña ha sido guardado exitosamente'})
            
        else:
            
            return render(req, 'cambiar_password.html', {'formulario': formulario})
        
    else:
        
        formulario = PasswordChangeForm(user=req.user)
        
        return render(req, 'cambiar_password.html', {'formulario': formulario})
    

class avatar(LoginRequiredMixin, CreateView):
    
    model = Avatar
    template_name = "avatar.html"
    fields = ['imagen']
    success_url = '/'

    def form_valid(self, form):
        # Asignar el usuario logueado al avatar
        form.instance.usuario = self.request.user
        
        # Si el usuario ya tiene un avatar, lo elimino antes de crear uno nuevo
        if self.request.user.avatar.exists():
            self.request.user.avatar.first().delete()
        
        return super().form_valid(form)

@login_required()
def perfil(req):
    
    usuario = req.user
    
    return render(req, 'perfil.html', {'usuario': usuario})

def denegado(req):
    
    return render(req, 'denegado.html', {})


### VIEWS PARA LOS CARRITOS DE COMPRAS Y LOS ARTíCULOS De ÉSTE ###

class CarritoView(LoginRequiredMixin, View):
    
    def get(self, req):
        carrito, created = Carrito.objects.get_or_create(usuario=req.user)
        items = carrito.items.all()
        total = sum(item.producto.precio * item.cantidad for item in items)
        return render(req, 'carrito.html', {'items': items, 'total': total})
    
class AgregarItemView(LoginRequiredMixin, View):
    
    def post(self, req, producto_id):
        # Obtengo o crea el carrito para el usuario si no existe
        carrito, created = Carrito.objects.get_or_create(usuario=req.user)
        
        # Obtén el producto basado en el producto_id pasado en la URL
        producto = Producto.objects.get(id=producto_id)
        
        # Agrega o actualiza el item del carrito
        item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
        item.cantidad += 1  # Incrementa la cantidad si ya existe en el carrito
        item.save()
        
        # Redirige al carrito para ver los productos agregados
        return redirect('carrito')
    
class EliminarItemView(LoginRequiredMixin, View):
    
    def post(self, request, item_id):
        item = CarritoItem.objects.get(id=item_id)
        item.delete()
        return redirect('carrito')
    
### CREAR PEDIDO ###
class PedidoView(LoginRequiredMixin, View):
    def post(self, request):
        # Obtener el carrito del usuario logueado
        carrito = Carrito.objects.get(usuario=request.user)
        items = carrito.items.all()
        
        # Si el carrito está vacío, redirige al carrito
        if not items:
            return redirect('carrito')

        # Calcular el total del pedido
        total = sum(item.producto.precio * item.cantidad for item in items)

        # Crear un pedido
        pedido = Pedido.objects.create(usuario=request.user, total=total)

        # Crear los items del pedido basados en el carrito
        for item in items:
            PedidoItem.objects.create(
                pedido=pedido,
                producto=item.producto,
                cantidad=item.cantidad,
                precio=item.producto.precio  # El precio en el momento de la compra
            )
        
        # Vaciar el carrito después de crear el pedido
        items.delete()

        return render(request, 'pedido_exitoso.html', {'pedido': pedido})
    

class PedidoDetalleView(LoginRequiredMixin, View):
    def get(self, request, pedido_id):
        # Obtener el pedido por ID
        pedido = Pedido.objects.get(id=pedido_id)
        items = pedido.items.all()
        return render(request, 'pedido_detalle.html', {'pedido': pedido, 'items': items})
    
class PedidoListarView(LoginRequiredMixin, View):
    def get(self, request):
        pedidos = request.user.pedidos.all()  # Usando related_name 'pedidos'
        return render(request, 'pedido_mis_pedidos.html', {'pedidos': pedidos})