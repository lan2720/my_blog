from django.contrib import admin
from article.models import Article,Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
