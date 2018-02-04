from django.contrib import admin
from .models import Book, Author, Read, Category, Write, Favor

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Read)
admin.site.register(Write)
admin.site.register(Favor)