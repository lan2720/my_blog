# coding:utf-8
from django.shortcuts import render
from article.models import Article,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    return render(request, 'article/home.html', {'articles':articles} )

def post(request, post_id = '1'):
    post = Article.objects.get(id = post_id) 
    return render(request, 'article/detail.html', {'post':post})

def archive(request):
    date_list = Article.objects.all()
    return render(request, 'article/archive.html', {'date_list':date_list})

def archive_year(request, year=''):
    article_list = Article.objects.filter(pub_date__year = year)
    return render(request, 'article/archive_year.html', {'article_list':article_list})

def archive_month(request, year, month):
    article_list = Article.objects.filter(pub_date__year = year, pub_date__month = month)
    return render(request, 'article/archive_year.html', {'article_list':article_list})

def category(request, category_name = ''):
    articles = Category.objects.get(name = category_name).articles.all()
    return render(request, 'article/category.html', {'articles':articles, 'category':category_name})

def category_index(request): # 主页上的category入口, 展示所有的category
    articles = Article.objects.all()
    return render(request, 'article/category_index.html', {'articles':articles})
