from django.db import models

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

def service_upload_to(instance, filename):
    if instance.pk == None:
        return 'service/'+filename
    else:
        old_instance = Service.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'service/'+filename

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Servicio")
    subtitle = models.CharField(max_length=100, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(upload_to=service_upload_to, verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Servicio"

    def __str__(self):
        return self.title