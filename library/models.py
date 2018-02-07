from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=(30))


class Book(models.Model):
	"""docstring for Book"""
	title = models.CharField(max_length=100)
	published_date = models.DateField()
	summary = models.TextField()
	language = models.CharField(max_length=50)
	link = models.URLField(max_length=200)
	pic = models.ImageField(upload_to = 'book') #author is a folder in MEDIA_ROOT
	categories = models.ManyToManyField(Category)
	users = models.ManyToManyField(User, through='Read')


class Author(models.Model):
	"""docstring for Author"""
	full_name = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	date_of_death = models.DateField(null=True)
	url = models.URLField(null=True)
	bio = models.TextField()
	pic = models.ImageField(upload_to = 'author') #author is a folder in MEDIA_ROOT
	books = models.ManyToManyField(Book, through='Write')


class Read(models.Model):
	"""docstring for Read"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	rate = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)], null=True)
	status_choices =   (('R', 'R'), ('W', 'W'), ('C', 'C'))
	status = models.CharField(max_length=1, choices=status_choices, null=True)

class Write(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)