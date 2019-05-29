from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article, Category, Tag, Tui, Banner, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#TODO:全局变量
def global_variable(request):
    hot = Article.objects.all().order_by('-views')[0:10]
    hottui = Article.objects.filter(tui_id=2)[0:10]
    alltag = Tag.objects.all()
    allCategory = Category.objects.all()
    return locals()


# TODO:首页
def index(request):
    banner = Banner.objects.filter(is_active=True)[0:3]
    tui = Article.objects.filter(tui=1)[0:3]
    newten = Article.objects.all().order_by('-id')[0:10]
    return render(request, 'blog/index.html', locals())

# TODO:列表页
def list(request):
    lid = request.GET['lid']
    categoryname = Category.objects.get(id=lid)
    list = Article.objects.filter(category_id=lid).order_by('created')
    # 分页
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', locals())


# TODO:内容页
def show(request):
    tid = request.GET['tid']
    cid = request.GET['cid']
    article = Article.objects.get(id=tid)
    category = Category.objects.get(id=cid)
    tag = Tag.objects.filter(article__id=tid)
    next_blog = Article.objects.filter(created__gt=article.created, category=article.category.id).first()
    provious_blog = Article.objects.filter(created__lt=article.created, category=article.category.id).last()
    article.views +=1
    article.save()
    eqtag_article = Article.objects.filter(tags__id=tid)
    return render(request, 'blog/show.html', locals())


# TODO:标签页
def tag(request):
    tid = request.GET['tid']
    tagname = Tag.objects.get(id=tid)
    list = Article.objects.filter(tags__id=tid).order_by('created')
    # 分页
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/tag.html', locals())



# TODO:搜索页
def search(request):
    ss = request.GET['name']
    # 获取搜索关键词通过标题进行匹配
    list = Article.objects.filter(title__icontains=ss)
    page = request.GET.get('page')
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'blog/search.html', locals())


# TODO:关于我们
def about(request):
    allCategory = Category.objects.all()
    return render(request, 'blog/page.html', locals())