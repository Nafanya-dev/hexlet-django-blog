from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "index.html"

    def get(self, request):
        return redirect(reverse("article", kwargs={'id':1}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def about(request):
    return render(request, 'about.html')

