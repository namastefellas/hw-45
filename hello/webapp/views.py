from django.shortcuts import render
from webapp.models import Article

# Create your views here.

def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', context={'articles': articles})