from django.shortcuts import render
from django.views.generic import ListView


class MainView(ListView):
    template_name = "mailing/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

