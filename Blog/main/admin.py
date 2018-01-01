from django.contrib import admin

from .models import Article 
from .models import Page



admin.site.register(Article)
admin.site.register(Page)