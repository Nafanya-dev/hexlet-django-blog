from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm


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


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        url = reverse('articles_create')
        return render(request, 'articles/create.html', {'form':form, 'url':url})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        url = reverse('articles_create')
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, 'articles/create.html', {'form':form, 'url':url})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        url = reverse('article_edit', kwargs={'id': article_id})
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request,
                      'articles/update.html',
                      {'form':form, 'url':url})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        url = reverse('article_edit', kwargs={'id': article_id})
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request,
                      'articles/update.html',
                      {'form':form, 'url':url})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect('articles')
