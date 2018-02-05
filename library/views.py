from django.shortcuts import render
from django.http import HttpResponse
from library.models import Book


# Create your views here.
def book(request, Id):
	# book = Book.objects.get(id = Id)
	book = ""
	return render(request, 'library/Book.html', {"book":book})
	