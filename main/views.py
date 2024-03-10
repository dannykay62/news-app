from django.shortcuts import render
from .models import News, Category


def index(request):
    first_news = News.objects.first()
    four_news = News.objects.all()[1:5]
    three_categories = Category.objects.all()[0:3]

    return render(request, 'index.html', {
        'first_news': first_news,
        'four_news': four_news,
        'three_categories': three_categories
    })
