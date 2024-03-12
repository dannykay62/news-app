from django.shortcuts import render
from .models import News, Category


# Home page
def index(request):
    first_news = News.objects.first()
    four_news = News.objects.all()[1:5]
    three_categories = Category.objects.all()[0:3]
    all_categories = Category.objects.all()

    return render(request, 'index.html', {
        'first_news': first_news,
        'four_news': four_news,
        'three_categories': three_categories,
        'all_categories': all_categories,
    })


# all news
def all_news(request):
    all_news = News.objects.all()
    return render(request, 'all-news.html', {
        'all_news': all_news
    })


# details page(full news)
def details(request, id):
    news = News.objects.get(pk=id)
    category = Category.objects.get(id=news.category.id)
    related_news = News.objects.filter(category=category).exclude(id=id)
    return render(request, 'details.html', {
        'news': news,
        'related_news': related_news,
    })


# Show all categories
def all_categories(request):
    all_cats = Category.objects.all()
    return render(request, 'categories.html', {
        'all_cats': all_cats,
    })


# Show a category
def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'all_news': news,
        'category': category,
    })