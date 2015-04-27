from django.conf.urls import url

urlpatterns = [
        url(r'^$', 'article.views.home', name = 'home'),
        url(r'^archive/$', 'article.views.archive', name = 'archive'),
        url(r'^archive/(?P<year>\d{4})/$', 'article.views.archive_year', name = 'archive_year'),
        url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', 'article.views.archive_month', name = 'archive_month'),
        url(r'^post/(?P<post_id>\d+)/', 'article.views.post', name='post'),
        url(r'^category/$', 'article.views.category_index', name='category_index'),
        url(r'^category/(?P<category_name>\w+)/', 'article.views.category', name='category'),
        ]

