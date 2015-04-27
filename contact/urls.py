from django.conf.urls import url

urlpatterns = [
        url(r'^$', 'contact.views.contact', name = 'contact'),
        url(r'^thanks/$', 'contact.views.thanks', name = 'thanks'),
        ] 
 
