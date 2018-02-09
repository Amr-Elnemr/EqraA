from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from library.models import Book, Category, Read, Write, Author , User
from library.classes import BookDetail
from django.db.models import Avg
import json


# Create your views here.

def home(request):
	user = request.user
	categories = user.category_set.all()
	topRate = Read.objects.filter().order_by('-rate')[:5]
	topBooks = []
	for x in topRate:
		global topBooks
		book=Book.objects.get(id = x.book_id)
		authors_books = book.write_set.all()
		authors = [i.author for i in authors_books]
		bookdetail =BookDetail(book.id,book.title,authors,book.pic,book.summary)
		topBooks.append(bookdetail)
	yourbooks = user.read_set.all()
	userBooks = []
	for x in yourbooks:
		global userBooks
		book=Book.objects.get(id = x.book_id)
		authors_books = book.write_set.all()
		authors = [i.author for i in authors_books]
		bookdetail =BookDetail(book.id,book.title,authors,book.pic,book.summary)
		userBooks.append(bookdetail)
	return render(request, 'library/home.html', {'categories': categories, 'topBooks':topBooks, 'userBooks':userBooks})

def book(request, Id):
	book = Book.objects.get(id = Id)
	authors_books = book.write_set.all()
	authors = [i.author for i in authors_books]
	book_rate = round(book.read_set.aggregate(Avg('rate'))['rate__avg'],2)
	user_book = book.read_set.filter(user=request.user.id, book=book.id)
	user_rate = user_book[0].rate if user_book else 0
	user_status = user_book[0].status if user_book else 0
	return render(request, 'library/Book.html', {"book":book, "authors":authors, "book_rate": book_rate, "user_rate": user_rate, 'user_status':user_status})
	

def categories(request):
	categories = Category.objects.all()
	user = request.user
	favCategories =  user.category_set.all()
	return render(request,'library/categories.html',{"categories":categories,"favCategories":favCategories})
	
def search(request,q):
	query = request.GET.get("search",None)
	matchBooks = Book.objects.filter(title = query)
	books = []
	for x in matchBooks:
		global userBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.author.id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		books.append(bookdetail)
		data ={"books":books}
	HttpResponse("ghgujhjh")
	
def rate_apply(request, book_id):
	book = Book.objects.get(id=book_id)
	user = request.user
	read_obj = Read.objects.filter(book=book,user=request.user)
	read_obj = read_obj[0] if read_obj else 0
	rate = request.GET['rate'] if request.GET['rate']!='0' else (read_obj.rate if read_obj else 0)
	status = request.GET['status'] if request.GET['status']!='0' else (read_obj.status if read_obj else 0)
	if read_obj:
		read_obj.status = status
		read_obj.rate = rate
		read_obj.save()		
		return HttpResponse(json.dumps({'req_status':'ok'}))
	else:
		Read.objects.create(user=user, book=book, rate=rate, status=status)
		return HttpResponse(json.dumps({'req_status':'ok'}))


def category(request,Id):
	category = Category.objects.get(id = Id)
	catBooks = []
	books = category.book_set.all()
	for x in books:
		book=Book.objects.get(id = x.id)
		wAuthor = Write.objects.filter(book = book.id)
		authors = []
		for a in wAuthor:
			author = Author.objects.get(id = a.author.id)
			authors.append(author)
		# authors = book.author_set.all()
		bookdetail =BookDetail(book.id,book.title,authors,book.pic,book.summary)
		catBooks.append(bookdetail)
	
	return render(request,'library/category.html',{"category":category,"catBooks":catBooks})


def add_to_favorit(request,cat_id):
	category = Category.objects.get(id = cat_id)
	user = request.user
	cat_users = category.user.all()
	if user in cat_users:
		user.category_set.remove(user)
	else:
		user.category_set.add(user)

	return HttpResponse(json.dumps({'status':'ok'}))

#Author views
from django.views import generic
class show_author(generic.DetailView):
	context_object_name="Author"
	model=Author
	template_name="library/Author_detail.html"



