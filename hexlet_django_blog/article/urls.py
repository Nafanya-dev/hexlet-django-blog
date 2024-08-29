from django.urls import path

from hexlet_django_blog.article.views import IndexView, IndexViews


urlpatterns = [
    path('<int:id>/',
    IndexView.as_view(),
    name='article'),
    path('', IndexViews.as_view()),
]

