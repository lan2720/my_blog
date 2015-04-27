from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'djblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'article.views.home', name = 'home'),
    url(r'^', include('article.urls', namespace = 'article')),
    url(r'^about/$', include('about_me.urls')),
    url(r'^contact/', include('contact.urls', namespace = 'contact')), 
    #url(r'^blog/(?P<post_title>\w+)$', 'article.views.detail', name = 'detail'),
    #url(r'^tag/(?P<tag_title>\w+)$', 'tag.views.detail', name = 'tag'),
]
