from django.views.generic import TemplateView
from .models import History, Cover

# Create your views here.
class HistoryPageView(TemplateView):
    template_name = "history/history.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        print(type(context))
        context['history'] = History.objects.first()
        context['cover'] = Cover.objects.first()
        return context
