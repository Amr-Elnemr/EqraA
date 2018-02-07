from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book
from library.models import Category
from library.models import Read
from library.models import Write
from library.models import Author
from library.classes import BookDetail
from django.db.models import Avg


# Create your views here.

def home(request,Id):
	categories = Category.objects.all()
	topRate = Read.objects.filter().order_by('rate')[:5]
	topBooks = []
	for x in topRate:
		global topBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.Author_id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		topBooks.append(bookdetail)
	yourbooks = Read.objects.filter(user_id = Id)
	userBooks = []
	for x in yourbooks:
		global userBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.Author_id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		userBooks.append(bookdetail)
	return render(request, 'library/home.html', {'categories': categories, 'topBooks':topBooks, 'userBooks':userBooks})

def book(request, Id):
	book = Book.objects.get(id = Id)
	authors_books = book.write_set.all()
	authors = [i.author for i in authors_books]
	book_rate = round(book.read_set.aggregate(Avg('rate'))['rate__avg'],2)
	user_rate = book.read_set.filter(user=request.user.id, book=book.id)
	user_rate = user_rate[0].rate if book_rate else 0
	return render(request, 'library/Book.html', {"book":book, "authors":authors, "book_rate": book_rate, "user_rate": user_rate})
	

def rate_apply(request, book_id, rate, status):
	book = Book.objects.get(id=book_id)
	read_obj = Read.objects.filter(book=book,user=request.user)
	read_obj = read_obj if read_obj else 0
	if read_obj:
		read_obj.status = status
		read_obj.rate = rate
		read_obj.save()
