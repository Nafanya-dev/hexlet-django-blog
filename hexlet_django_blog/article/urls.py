from django.urls import path

from hexlet_django_blog.article.views import IndexView, IndexViews, ArticleFormCreateView


urlpatterns = [
    path('<int:id>/',
    IndexView.as_view(),
    name='article'),
    path('', IndexViews.as_view(), name='articles'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]

