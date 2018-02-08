from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book
from library.models import Category
from library.models import Read
from library.models import Write
from library.models import Author
from library.classes import BookDetail
from django.db.models import Avg
from django.views import View
from django.contrib.auth.models import User
from .forms import EditProfile
# Create your views here.

def home(request,Id):
	categories = Category.objects.all()
	topRate = Read.objects.filter().order_by('rate')[:5]
	topBooks = []
	for x in topRate:
		# global topBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.Author_id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		topBooks.append(bookdetail)
	yourbooks = Read.objects.filter(user_id = Id)
	userBooks = []
	for x in yourbooks:
		# global userBooks
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
	book_rate = book.read_set.aggregate(Avg('rate'))['rate__avg']
	return render(request, 'library/Book.html', {"book":book, "authors":authors, "book_rate": book_rate})


class ProfileView(View):
	def  get(self, request):
		user = request.user
		read_book = user.read_set.all()
		books = [i.book for i in read_book]
		status = [j.status for j in read_book]
		# user = User.objects.filter(id=id)[0]
		return render (request, 'library/profile_page.html', {'user': user, 'books': books, 'status': status})
	
def edit_profile(request):
	if request.method=='POST':
		form = EditProfile(request.POST)
		if form.is_valid():
			user = form.save(commit=false)
			user.set_password(user.password)
			form.save()
			return HttpResponse("updated")
	elif request.method=='GET':
		form = EditProfile()
		return render(request, 'library/edit_profile.html', {'form': form})