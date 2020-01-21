from django.views.generic.detail import DetailView
from .models import Page, Cover

# Create your views here.
class LegalPageView(DetailView):
    model=Page
    template_name = "information/sample.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['cover'] = Cover.objects.first()
        return context