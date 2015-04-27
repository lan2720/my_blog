# coding: utf-8
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 30) # category name

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Article(models.Model):
    title = models.CharField(max_length = 100) # 博客题目
    category = models.ForeignKey(Category, related_name = 'articles') # 一篇文章只放在一个category下，但是每个category有很多文章
    #pub_date = models.DateTimeField(auto_now_add = True) # 发表时间
    pub_date = models.DateTimeField(editable = True) # 发表时间
    content = models.TextField() # 博客正文

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-pub_date',)


