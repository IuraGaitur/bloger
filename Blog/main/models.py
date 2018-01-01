from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	author = models.CharField(max_length=255)
	create_date = models.DateTimeField(blank = True, null = True)
	category = models.CharField(max_length = 255)
	small_image  = models.TextField()
	big_image = models.TextField()

	def __str__(self):
   		return 'Article: ' + self.title

class Page(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.TextField(blank = True, null = True)

	def __str__(self):
   		return 'Page: ' + self.title