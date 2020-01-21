from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cover,TimeTable, Visit

# Create your views here.
class VisitPageView(TemplateView):
    template_name = "visit/visit.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['visit'] = Visit.objects.first()
        context['timeTable'] = TimeTable.objects.all()
        context['cover'] = Cover.objects.first()
        return context