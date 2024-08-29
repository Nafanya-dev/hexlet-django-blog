from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article


class IndexView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request,'articles/index.html',
		      context={'article': article},
		     )


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request,
                      'articles/index_views.html',
                      context={'articles': articles}
                      )
