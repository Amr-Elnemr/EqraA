from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book, name="book"),
    re_path(r'^book/([0-9]+)/edit$', views.rate_apply, name="edit_book"),
    re_path(r'^home/(?P<Id>[0-9]+)/$',views.home, name='home'),
    path('search/',views.search, name='search'),
    path('categories/',views.categories),
    path('author/<int:pk>', views.show_author.as_view(), name='show_author'),
    re_path(r'^register/$', views.UserFormView.as_view(), name='register')
]