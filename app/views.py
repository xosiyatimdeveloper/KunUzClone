from django.shortcuts import render, get_object_or_404
from .models import Category, News


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html', context=context)

def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context=context)

def home_page(request):
    news_list = News.objects.filter(status=News.Status.Published)
    mixin_news = News.published.all().order_by('-publish_time')[:4]
    uzb_news_1 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[0]
    uzb_news_2 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[1]
    uzb_news_3 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[2]
    uzb_news_4 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[3]
    jahon_news = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[:5]
    fan_news_1 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[0]
    fan_news_2 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[1]
    fan_news_3 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[2]
    fan_news_4 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[3]
    context = {
        'news_list': news_list,
        'mixin_news': mixin_news,
        'uzb_news_1': uzb_news_1,
        'uzb_news_2': uzb_news_2,
        'uzb_news_3': uzb_news_3,
        'uzb_news_4': uzb_news_4,
        'jahon_news': jahon_news,
        'fan_news_1': fan_news_1,
        'fan_news_2': fan_news_2,
        'fan_news_3': fan_news_3,
        'fan_news_4': fan_news_4
    }

    return render(request, 'news/index.html', context=context)

def uzb_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/uzbekistan.html', context=context)

def jahon_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/jahon.html', context=context)

def sport_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/sport.html', context=context)

def fan_page(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/fan.html', context=context)



