from django.db import models
from ckeditor.fields import RichTextField

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

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0, help_text="Ayuda a ordenar los links en el footer")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ["order","title"]

    def __str__(self):
        return self.title