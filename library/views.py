from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from library.forms import userform
from django.http import HttpResponse
from django.http import JsonResponse
from library.models import Book, Category, Read, Write, Author
from library.classes import BookDetail
from django.db.models import Avg
import json
from django.contrib.auth.models import User
from .forms import EditProfile

# Create your views here.

def home(request,Id):
	categories = Category.objects.all()
	topRate = Read.objects.filter().order_by('-rate')[:5]
	topBooks = []
	for x in topRate:
		# global topBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.author.id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		topBooks.append(bookdetail)
	yourbooks = Read.objects.filter(user_id = Id)
	userBooks = []
	for x in yourbooks:
		# global userBooks
		book=Book.objects.get(id = x.book_id)
		wAuthor = Write.objects.get(book = book.id)
		author = Author.objects.get(id = wAuthor.author.id)
		bookdetail =BookDetail(book.id,book.title,author.id,author.full_name,book.pic,book.summary)
		userBooks.append(bookdetail)
	return render(request, 'library/home.html', {'categories': categories, 'topBooks':topBooks, 'userBooks':userBooks})


#Book details
def book(request, Id):
	book = Book.objects.get(id = Id)
	authors_books = book.write_set.all()
	authors = [i.author for i in authors_books]
	book_rate = book.read_set.aggregate(Avg('rate'))['rate__avg']
	book_rate = round(book_rate, 2) if book_rate else 0
	user_book = book.read_set.filter(user=request.user.id, book=book.id)
	user_rate = user_book[0].rate if user_book else 0
	user_status = user_book[0].status if user_book else 0
	return render(request, 'library/Book.html', {"book":book, "authors":authors, "book_rate": book_rate, "user_rate": user_rate, 'user_status':user_status})
	

def categories(request):
	categories = Category.objects.all() 
	books={}
	for x in categories:
		book_cat=x.book_set.all()[:4]
		books[x.name]=book_cat
	# 	books.append(book_cat)
	return render(request,'library/categories.html',{"categories":categories,"books":books})
	
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
	

#Book rate and status
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

#Author views
from django.views import generic
class show_author(generic.DetailView):
	context_object_name="Author"
	model=Author
	template_name="library/Author_detail.html"

#Registarion Form:
class UserFormView(View):
	form_class=userform
	template_name='library/registration.html'

	def get(self, request):
		form=self.form_class(request.POST)

		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#Authentication:
			user=authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('library:home')
		return render(request, self.template_name, {'form':form})


###########
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