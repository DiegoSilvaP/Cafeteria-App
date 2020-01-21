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

class History(models.Model):
    title = models.CharField(max_length=250, verbose_name="Título de la historia")
    subtitle = models.CharField(max_length=250, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historia"
    
    def __str__(self):
        return self.title