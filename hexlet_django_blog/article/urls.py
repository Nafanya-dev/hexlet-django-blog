from django.urls import path

from hexlet_django_blog.article.views import(
IndexView,
IndexViews,
ArticleFormCreateView,
ArticleFormEditView,
ArticleFormDeleteView,
)


urlpatterns = [
    path('<int:id>/edit/', ArticleFormEditView.as_view(), name='article_edit'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>/',
    IndexView.as_view(),
    name='article'),
    path('', IndexViews.as_view(), name='articles'),
    path('create/', ArticleFormCreateView.as_view(), name='articles_create'),
]

