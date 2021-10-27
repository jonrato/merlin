from django.shortcuts import render
from django.views.generic import TemplateView
from analises.models import FileHandler
from analises.models import FileHandlerForm

class IndexView(TemplateView):
    template_name=''

    def def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {'form', FileHandlerForm}
    