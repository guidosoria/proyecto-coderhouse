from App_iShop.models import Avatar

def avatar_context(req):
    if req.user.is_authenticated:
        try:
            avatar_url = req.user.avatar.imagen.url
        except Avatar.DoesNotExist:
            avatar_url = '/media/img/avatars/default.jpg'  # Ruta de la imagen por defecto
    else:
        avatar_url = None
    return {'avatar_url': avatar_url}