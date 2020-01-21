from django.db import models
from django.core.validators import RegexValidator

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

class Footer(models.Model):
    image = models.ImageField(upload_to=custom_upload_to, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name_plural = "Footer"

    def __str__(self):
        return self.image.url

def index_upload_to(instance, filename):
    # 'instance' hace referencia al objeto que se esta guardando, pero despues de que se haya confirmado el nuevo valor,
    # en 'filename tendremos el nombre del fichero con la imagen que queremos sobreescribir
    if instance.pk == None:
        return 'index/'+filename
    else:
        old_instance = Index.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'index/'+filename


class Index(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título", help_text="Título del post de la primera página", blank=True)
    subtitle = models.CharField(max_length=150, verbose_name="Subtítulo", blank=True)
    paragraphTitle = models.CharField(max_length=150, verbose_name="Título del párrafo", blank=True)
    content = models.TextField(verbose_name="Párrafo")
    image = models.ImageField(upload_to=index_upload_to, verbose_name="Imagen", help_text="Imagen del post de la primera página", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name_plural="Index"

    def __str__(self):
        return self.content[:50]+"..."

class Link(models.Model):
    key = models.SlugField( max_length=100, unique=True)
    name = models.CharField( max_length=200, verbose_name="Red social")
    url = models.URLField( max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "link"

    def __str__(self):
        return self.name

PHONE_CHOICES = (
    ('Casa', 'Casa'),
    ('Oficina', 'Oficina')
)

class Phone(models.Model):
    type = models.CharField(max_length=10, choices=PHONE_CHOICES, verbose_name="Tipo", default=0)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10,10}$')], verbose_name="Teléfono", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Teléfono"

    def __str__(self):
        return self.type

def logo_upload_to(instance, filename):
    print("LOGO ",instance, filename)
    if instance.pk == None:
        return 'logo/'+filename
    else:
        old_instance = Logo.objects.get(pk=instance.pk)
        old_instance.icon.delete()
        return 'logo/'+filename

class Logo(models.Model):
    name = models.CharField(max_length=10,verbose_name="Nombre", default="Logo")
    icon = models.ImageField(upload_to="logo", verbose_name="Logo", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name_plural="Logo"

    def __str__(self):
        if self.icon:
            return self.icon.url
        else:
            return "No Icon"