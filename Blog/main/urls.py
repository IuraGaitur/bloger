from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.articles, name='index'),
    url(r'archives$', views.archives, name='archives'),
    url(r'about$', views.about, name='about'),
    url(r'contacts$', views.contacts, name='contacts'),
    url(r'article/(?P<article_id>\d+)$', views.article, name='article')
]
