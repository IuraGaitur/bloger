from django.shortcuts import render
from .models import Article
from .models import Page

# Create your views here.

def articles(request):
	items = Article.objects.all().order_by("-id")[:4]
	firstArticle = items[0]
	items = items[1:4]

	page = Page.objects.get(title='About')
	data = {'articles': items, 'about': page, 'firstArticle': firstArticle}
	return render(request, 'index.html', data)

def archives(request):
	items = Article.objects.all().order_by("-id")
	data = {'articles': items}
	return render(request, 'archives.html', data)

def about(request):
	page = Page.objects.get(title='About')
	data = {'info': page}
	return render(request, 'about.html', data)

def contacts(request):
	page = Page.objects.get(title='Contact')
	data = {'info': page}
	return render(request, 'contact.html', data)

def article(request, article_id):
	article = Article.objects.get(id = article_id)
	data = {'article': article}
	return render(request, 'article.html', data)







    

