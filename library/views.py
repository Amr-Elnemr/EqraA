from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book
from library.models import Category
from library.models import Read
from library.models import Write
from library.models import Author
from library.classes import BookDetail


# Create your views here.

def home(request,id):
	categories = Category.objects.all()
	topRate = Read.objects.filter().order_by('rate')[:5]
	topBooks = []
	for x in topRate:
		global topBooks
		book=Book.objects.get(id = x.book)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.Author)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name)
		topBooks.append(bookdetail)
	return render(request, 'library/home.html', {'categories': categories, 'topBooks':topBooks})

def book(request, Id):
	book = Book.objects.get(id = Id)
	book = ""
	return render(request, 'library/Book.html', {"book":book})
	
