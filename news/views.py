from django.shortcuts import render
from news.models import News


def main(request):
    news = News.objects.all()
    return render(request, 'index.html', {'news': news})


def item_news(request, id):
    news = News.objects.get(id=id)
    return render(request, 'item_news.html', {'news': news})

# Create your views here.
