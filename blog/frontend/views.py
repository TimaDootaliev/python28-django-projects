from django.shortcuts import render
from article.models import Article

# Create your views here.


def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'frontend/articles.html', {'articles': articles})