from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book, name="book"),
    re_path(r'^book/([0-9]+)/edit$', views.rate_apply, name="edit_book"),
    path('home/',views.home, name='home'),
    re_path(r'^category/(?P<Id>[0-9]+)/$',views.category,name='category'),
    re_path(r'^category/([0-9]+)/fav$', views.add_to_favorit, name="favorite_cat"),
    path('search/',views.search, name='search'),
    path('categories/',views.categories,name="categories"),
    path('author/<int:pk>', views.show_author.as_view(), name='show_author'),
]