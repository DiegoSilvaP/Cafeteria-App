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

class Visit(models.Model):
    header = models.CharField(max_length=100, verbose_name="Encabezado")
    subheader = models.CharField(max_length=100, verbose_name="Subencabezado")
    addressLine1 = models.CharField(max_length=200, verbose_name="Dirección (linea 1)")
    addressLine2 = models.CharField(max_length=200, verbose_name="Dirección (linea 2)", blank=True)
    phoneNumber = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10,10}$')], verbose_name="Teléfono", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Página de visita"
        verbose_name_plural="Página de visita"
    
    def __str__(self):
        return self.header

DAYS_CHOICES = (
    ('Lunes', 'Lunes'),
    ('Martes', 'Martes'),
    ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'),
    ('Viernes', 'Viernes'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
)


def fill_hourslist():
    HOURS_CHOICES = ()
    for x in range(24):
        HOURS_CHOICES = HOURS_CHOICES + ((x, str(x)+":00"),)
    return HOURS_CHOICES
    

class TimeTable(models.Model):
    FromDay = models.CharField(max_length=10, choices= DAYS_CHOICES, default="Lunes", verbose_name="De")
    ToDay = models.CharField(max_length=10, choices= DAYS_CHOICES, default="Viernes", verbose_name="A")
    FromHour = models.IntegerField(choices=fill_hourslist(), default=8, verbose_name="De")
    ToHour = models.IntegerField(choices=fill_hourslist(), default=20, verbose_name="A")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Horario"

    def __str__(self):
        return self.FromDay+" - "+self.ToDay