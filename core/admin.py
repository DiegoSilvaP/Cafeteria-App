from django.contrib import admin
from .models import Cover, Index, Footer, Link, Phone, Logo

# Register your models here.
admin.site.register(Cover)
admin.site.register(Footer)
admin.site.register(Index)

class LogoAdmin(admin.ModelAdmin):
    readonly_fields=('name',)

admin.site.register(Logo,LogoAdmin)

class PhoneAdmin(admin.ModelAdmin):
    list_display=('type','phoneNumber')

admin.site.register(Phone,PhoneAdmin)

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('key','name','created', 'updated')
    list_display = ('name','url','updated','created',)
    search_fields = ['name','url']
    list_filter = ('name',)
    
admin.site.register(Link, LinkAdmin)