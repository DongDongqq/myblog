from django.contrib import admin
# Todo:导入需要管理的数据库表
from .models import Banner, Category, Tag, Tui, Article, Link

# Register your models here.
admin.site.site_header = 'Django中文网管理后台'
admin.site.site_title = 'Django中文网'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'user', 'views', 'created')
    # 满五十条数据自动分页
    list_per_page = 50
    # 后台数据列表默认排序方式
    ordering = ('-created',)
    # 设置哪些字段可以点击进入编辑页面
    list_display_links = ('id', 'title')
    # fk_fields 设置显示外键字段
    fk_fields = ['category']
    search_fields = ['title', 'id']


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class Tui(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')





