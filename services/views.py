from django.views.generic import ListView
from .models import Service, Cover

# Create your views here.
class ServicesPageView(ListView):
    model = Service
    template_name = "services/services.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context

