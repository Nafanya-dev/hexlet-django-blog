from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class IndexView(View):
    def get(self, request, tags, article_id):
        text = f"Статья номер {article_id}. Тег {tags}"
        return render(request,'articles/index.html',
		      context={'text': text},
		     )
