from django.shortcuts import render
from django.views.generic import ListView
from portal.models import Work


class MainView(ListView):
    model = Work
    template_name = "portal/main.html"
    extra_context = {'title': 'Главная страница'}


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

