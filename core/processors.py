from .models import Footer, Link, Phone, Logo

def footer(request):
    footer = Footer.objects.first()
    return {'FOOTER':footer.image.url}

def link(request):
    link_ctx = {}
    links = Link.objects.all()
    for link in links:
        link_ctx[link.key] = link.url
    return link_ctx

def phone(request):
    phone = Phone.objects.first()
    if phone:
        return {'PHONE':phone.phoneNumber}
    else:
        return {'PHONE':''}


def logo(request):
    logo = Logo.objects.first()
    print(logo)
    if logo.icon:
        return {'LOGO':logo.icon.url}
    else:
        return {'LOGO':''}
    
    