# Dar de alta mi template
from django import template
from information.models import Page

# Registrar mi template
register = template.Library()
# Creamos un decorador, es decir, transformamos una función normal 
# en un tag simple y lo registramos en la librería de templates
@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    print(pages)
    return pages

# Ahora, ya lo podemos usar en los templates
# NOTA: hay que registrar nuestro pages_extras en los templates
# con un {% load pages_extras %} y ya podremos llamarlo