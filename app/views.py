from django.shortcuts import render, get_object_or_404
from .models import Category, News


# Create your views here.

def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)

    context = {
        'news_list': news_list
    }

    return render(request, 'news/news_list.html', context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/comments.html', context)

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
    sport_news_1 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[0]
    sport_news_2 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[1]
    sport_news_3 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[2]
    sport_news_4 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[3]
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
        'fan_news_4': fan_news_4,
        'sport_news_1':sport_news_1,
        'sport_news_2': sport_news_2,
        'sport_news_3': sport_news_3,
        'sport_news_4': sport_news_4,
    }

    return render(request, 'news/index.html', context=context)

def uzb_page(request):
    uzb_news_1 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[0]
    uzb_news_2 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[1]
    uzb_news_3 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[2]
    uzb_news_4 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[3]
    uzb_news_5 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[4]
    uzb_news_6 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[5]
    uzb_news_7 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[6]
    uzb_news_8 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[7]
    uzb_news_9 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[8]
    uzb_news_10 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[9]
    uzb_news_11 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[10]
    uzb_news_12 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[11]
    uzb_news_13 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[12]
    uzb_news_14 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[13]
    uzb_news_15 = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[14]

    context = {
        'uzb_news_1': uzb_news_1,
        'uzb_news_2': uzb_news_2,
        'uzb_news_3': uzb_news_3,
        'uzb_news_4': uzb_news_4,
        'uzb_news_5': uzb_news_5,
        'uzb_news_6': uzb_news_6,
        'uzb_news_7': uzb_news_7,
        'uzb_news_8': uzb_news_8,
        'uzb_news_9': uzb_news_9,
        'uzb_news_10': uzb_news_10,
        'uzb_news_11': uzb_news_11,
        'uzb_news_12': uzb_news_12,
        'uzb_news_13': uzb_news_13,
        'uzb_news_14': uzb_news_14,
        'uzb_news_15': uzb_news_15,
    }

    return render(request, 'news/uzbekistan.html', context=context)

def jahon_page(request):
    jahon_news_1 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[0]
    jahon_news_2 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[1]
    jahon_news_3 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[2]
    jahon_news_4 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[3]
    jahon_news_5 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[4]
    jahon_news_6 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[5]
    jahon_news_7 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[6]
    jahon_news_8 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[7]
    jahon_news_9 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[8]
    jahon_news_10 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[9]
    jahon_news_11 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[10]
    jahon_news_12 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[11]
    jahon_news_13 = News.published.all().filter(category__name="Jahon").order_by('-publish_time')[12]




    context = {
        'jahon_news_1': jahon_news_1,
        'jahon_news_2': jahon_news_2,
        'jahon_news_3': jahon_news_3,
        'jahon_news_4': jahon_news_4,
        'jahon_news_5': jahon_news_5,
        'jahon_news_6': jahon_news_6,
        'jahon_news_7': jahon_news_7,
        'jahon_news_8': jahon_news_8,
        'jahon_news_9': jahon_news_9,
        'jahon_news_10': jahon_news_10,
        'jahon_news_11': jahon_news_11,
        'jahon_news_12': jahon_news_12,
        'jahon_news_13': jahon_news_13,
    }

    return render(request, 'news/jahon.html', context=context)

def sport_page(request):
    sport_news_1 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[0]
    sport_news_2 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[1]
    sport_news_3 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[2]
    sport_news_4 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[3]
    sport_news_5 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[4]
    sport_news_6 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[5]
    sport_news_7 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[6]
    sport_news_8 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[7]
    sport_news_9= News.published.all().filter(category__name="Sport").order_by('-publish_time')[8]
    sport_news_10 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[9]
    sport_news_11 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[10]
    sport_news_12 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[11]
    sport_news_13 = News.published.all().filter(category__name="Sport").order_by('-publish_time')[12]


    context = {
        'sport_news_1': sport_news_1,
        'sport_news_2': sport_news_2,
        'sport_news_3': sport_news_3,
        'sport_news_4': sport_news_4,
        'sport_news_5': sport_news_5,
        'sport_news_6': sport_news_6,
        'sport_news_7': sport_news_7,
        'sport_news_8': sport_news_8,
        'sport_news_9': sport_news_9,
        'sport_news_10': sport_news_10,
        'sport_news_11': sport_news_11,
        'sport_news_12': sport_news_12,
        'sport_news_13': sport_news_13,
    }

    return render(request, 'news/sport.html', context=context)

def fan_page(request):
    fan_news_1 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[0]
    fan_news_2 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[1]
    fan_news_3 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[2]
    fan_news_4 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[3]
    fan_news_5 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[4]
    fan_news_6 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[5]
    fan_news_7 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[6]
    fan_news_8 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[7]
    fan_news_9 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[8]
    fan_news_10 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[9]
    fan_news_11 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[10]
    fan_news_12 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[11]
    fan_news_13 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[12]

    context = {
        'fan_news_1': fan_news_1,
        'fan_news_2': fan_news_2,
        'fan_news_3': fan_news_3,
        'fan_news_4': fan_news_4,
        'fan_news_5': fan_news_5,
        'fan_news_6': fan_news_6,
        'fan_news_7': fan_news_7,
        'fan_news_8': fan_news_8,
        'fan_news_9': fan_news_9,
        'fan_news_10': fan_news_10,
        'fan_news_11': fan_news_11,
        'fan_news_12': fan_news_12,
        'fan_news_13': fan_news_13,
    }

    return render(request, 'news/fan.html', context=context)

def contact_page(request):
    fan_news_1 = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[0]

    context = {
        'fan_news_1': fan_news_1,
    }

    return render(request, 'news/contact.html', context=context)




