from django.db import models
# Importar la librería timezone
# from django.utils import timezone
from django.utils.timezone import now
# Importar el model de autenticación y usuarios de django
from django.contrib.auth.models import User

# Create your models here.

def custom_upload_to(instance, filename):
    if instance.pk == None:
        return 'covers/'+filename
    else:
        old_instance = Cover.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'covers/'+filename

class Cover(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen")
    header = models.CharField(max_length=150, blank=True, verbose_name="Encabezado del cover")
    paragraph = models.TextField(blank=True, verbose_name="Párrafor del cover")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    def __str__(self):
        return self.image.url
        
    class Meta:
        verbose_name_plural = "Cover"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Categoría")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    
    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.name

def post_upload_to(instance, filename):
    if instance.pk == None:
        return 'blog/'+filename
    else:
        old_instance = Post.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'blog/'+filename

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    # Establecida por el autor y por defecto tendrá la hora actual
    # NOTA esta es una forma correcta de registrar la hora actual, pero django estará esperando que coloquemos directamente el now, importando
    # django.utils.timezone.now en ves de from django.utils import timezone
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to=post_upload_to, blank=True)
    # # # # # image = models.ImageField(verbose_name="Imagen", upload_to="blog", blank=True, null=True)
    # Se enlazará con una clave foránea tomándola del modelo de usuarios de django
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # Se relacionará con varias categorias, (ya las tenemos arriba)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")


    # Hay que agregar una subclase para modificar los nombres y ponerlos en español
    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        # ordenamiento
        # por defecto, django ordena del más viejo al mas nuevo, por lo que se le agrega un -
        # para ordenar del mas nuevo al mas viejo
        ordering = ["-created"]

    def __str__(self):
        return self.title