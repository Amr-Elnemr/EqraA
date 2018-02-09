
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from library.forms import userform, loginform
from django.http import HttpResponse, JsonResponse
from library.models import Book, Category, Read, Write, Author, UserProfile
from library.classes import BookDetail
from django.db.models import Avg
import json
from django.contrib.auth.models import User
from .forms import EditProfile
from .forms import UpdateProfileImage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
	user = request.user
	categories = user.category_set.all()
	topRate = Read.objects.filter().order_by('-rate')[:5]
	topBooks = []
	for x in topRate:
		book=Book.objects.get(id = x.book_id)
		authors_books = book.write_set.all()
		authors = [i.author for i in authors_books]
		bookdetail =BookDetail(book.id,book.title,authors,book.pic,book.summary)

		topBooks.append(bookdetail)
	yourbooks = user.read_set.all()
	userBooks = []
	for x in yourbooks:
		# global userBooks
		book=Book.objects.get(id = x.book_id)
		authors_books = book.write_set.all()
		authors = [i.author for i in authors_books]
		bookdetail =BookDetail(book.id,book.title,authors,book.pic,book.summary)
		userBooks.append(bookdetail)
	return render(request, 'library/home.html', {'categories': categories, 'topBooks':topBooks, 'userBooks':userBooks})


#Book details
@login_required
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
	
@login_required
def categories(request):
	categories = Category.objects.all()
	user = request.user
	favCategories =  user.category_set.all()
	return render(request,'library/categories.html',{"categories":categories,"favCategories":favCategories})

@login_required
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
@login_required
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


@login_required
def category(request,Id):
	category = Category.objects.get(id = Id)
	catBooks = []
	user = request.user
	fav = True if user in category.user.all() else False
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
	
	return render(request,'library/category.html',{"category":category,"catBooks":catBooks,"fav":fav})

@login_required
def add_to_favorit(request,cat_id):
	category = Category.objects.get(id = cat_id)
	user = request.user
	cat_users = category.user.all()
	favorite = True
	if user in cat_users:
		category.user.remove(user)
		favorite = False
	else:
		category.user.add(user)

	return HttpResponse(json.dumps({'favorite':favorite}))

#Author views
from django.views import generic
class show_author(generic.DetailView):
	context_object_name="Author"
	model=Author
	template_name="library/Author_detail.html"

#Registarion Form:
errMsg="!One or more entries are not valid, please try again."
class UserFormView(View):
	form_class=userform
	template_name='library/registration.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		# check non existance:
		if User.objects.filter(username=form.data['username']).exists():
			inMsg='sorry but this username is already taken'
			return render(request, self.template_name, {'error': inMsg})
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()
		else:
			return render(request, self.template_name, {'error':errMsg})

		# Authentication:
		user=authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('library:home')
		return render(request, self.template_name, {'error':errMsg})

#Login Form:
LogerrMsg='Sorry, but your username or password is incorrect.'
class loginform(View):
	form_class=loginform
	template_name='library/login.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		username=form.data['username']
		password=form.data['password']
		# check authentication:
		loggedUser = authenticate(username=username, password=password)
		if loggedUser is not None:
			if loggedUser.is_active:
				login(request, loggedUser)
				return redirect('library:home')
		return render(request, self.template_name, {'error':LogerrMsg})

###########################################



@login_required
def search_all(request):
	search_word = request.GET['k'] if request.GET['k'] != "0" else 0
	if search_word:
		books = Book.objects.filter(title__icontains=search_word)[:5]
		authors = Author.objects.filter(full_name__icontains=search_word)[:5]
		all_ids = ["book"+str(i.id) for i in books] + ["author"+str(i.id)for i in authors]
		books = [{'title':i.title, 'id':i.id} for i in books]
		authors = [{'full_name':i.full_name, 'id':i.id} for i in authors]
		if books or authors:
			return HttpResponse(json.dumps({'req_status':'ok', 'data':{'books':books, 'authors':authors, 'all_ids':all_ids}}))
		else:
			return HttpResponse(json.dumps({'req_status':'not_found'}))
	else:
		return HttpResponse(json.dumps({'req_status':'not_found'}))


class ProfileView(View):
	def  get(self, request):
		user = request.user
		read_book = user.read_set.all()
		books = [i.book for i in read_book]
		status = [j.status for j in read_book]
		# user = User.objects.filter(id=id)[0]
		return render (request, 'library/profile_page.html', {'user': user, 'books': books, 'status': status})

@login_required	
def edit_profile(request):
	if request.method=='POST':
		form = EditProfile(request.POST)
		if form.is_valid():
			user = request.user
			form_data=form.cleaned_data
			user.first_name = form_data['first_name']
			user.last_name = form_data['last_name']
			user.set_password(form_data['password'])
			user.save()
			user = authenticate(username=user.username, password=user.password)
			login(request, user)
			# userf = form.save(commit=False)
			# user.set_password(userf.password)
			# user=form.save()
			return redirect('/library/profile_page')
			# return HttpResponse("updated")
		else:
			return render(request, 'library/edit_profile.html', {'form': form})
	elif request.method=='GET':
		form = EditProfile()
		return render(request, 'library/edit_profile.html', {'form': form})





@login_required
def advanced_search(request):
    search_word = request.GET['k'] if 'k' in request.GET.keys() else 0
    if search_word:
        books = Book.objects.filter(title__icontains=search_word)
        authors = Author.objects.filter(full_name__icontains=search_word)
        if books or authors:
            books = [i for i in books]
            authors = [i for i in authors]
            return render (request, 'library/search.html', {'data':{'books':books, 'authors':authors}})
        else:
            return render (request, 'library/search.html', {'data':{'books':[], 'authors':[]}})
    else:
        return render (request, 'library/search.html', {'data':{'books':[], 'authors':[]}})



####update profile image
@login_required
def update_profile_image(request):
	if request.method=='POST':
		form = UpdateProfileImage(request.POST, request.FILES)
		if form.is_valid():
			form_data=form.cleaned_data
			userprofile = request.user.userprofile
			userprofile.pic = form_data['pic']
			userprofile.save()
			return redirect('/library/profile_page')
			# return HttpResponse("updated")
	elif request.method=='GET':
		form = UpdateProfileImage()
		return render(request, 'library/edit_profile_image.html', {'form': form})



@login_required
def delete_me(request):
    user = request.user
    user = User.objects.get(id = user.id)
    user.delete()
    return redirect('/library/login')