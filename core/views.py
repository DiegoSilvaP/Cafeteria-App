from django.views.generic.base import TemplateView
# from django.views.generic import ListView
from .models import Index, Cover

# Create your views here.
class HomePageView(TemplateView):
    # model = Index
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['index'] = Index.objects.first()
        context['cover'] = Cover.objects.first()
        return context
