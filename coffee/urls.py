"""coffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('',include('core.urls')),
    path('historia/',include('history.urls')),
    path('servicios/',include('services.urls')),
    path('visitanos/',include('visit.urls')),
    path('contactanos/',include('contact.urls')),
    path('blog/',include('blog.urls')),
    path('informacion/',include('information.urls')),
]

admin.site.site_header = "CAFE Admin"
admin.site.site_title = "CAFE Admin Portal"
admin.site.index_title = "Bienvenido al portal de CAFE"

# Comprobar si estamos en debug
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)