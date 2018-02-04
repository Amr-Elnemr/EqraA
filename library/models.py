from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField(max_length=(30))
	users = models.ManyToManyField(User, through='Favor')


class Book(models.Model):
	"""docstring for Book"""
	title = models.CharField(max_length=100)
	published_date = models.DateField()
	summary = models.TextField(max_length=500)
	language = models.CharField(max_length=50)
	link = models.URLField(max_length=200)
	categories = models.ManyToManyField(Category)
	users = models.ManyToManyField(User, through='Read')


class Author(models.Model):
	"""docstring for Author"""
	full_name = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	date_of_death = models.DateField(null=True)
	url = models.URLField(null=True)
	bio = models.TextField(max_length=1000)
	books = models.ManyToManyField(Book, through='Write')


class Read(models.Model):
	"""docstring for Read"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	rate = models.SmallIntegerField(null=True)
	status_choices =   (('R', 'Read'), ('W', 'Wish'), ('C', 'Currently'))
	status = models.CharField(max_length=1, choices=status_choices)

class Write(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
		

class Favor(models.Model):
	"""docstring for Favor"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Category, on_delete=models.CASCADE)
