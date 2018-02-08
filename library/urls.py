from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book, name="book"),
    re_path(r'^home/(?P<Id>[0-9]+)/$',views.home, name='home'),
    # re_path(r'^author/$', views.all_writer_view),
    re_path(r'^profile_page/$', views.ProfileView.as_view()),
    re_path(r'^edit_profile/$', views.edit_profile),
    re_path(r'^book/([0-9]+)/edit$', views.rate_apply, name="edit_book"),
    re_path(r'^home/(?P<Id>[0-9]+)/$',views.home, name='home'),
    path('search/',views.search, name='search'),
    path('categories/',views.categories),
    path('author/<int:pk>', views.show_author.as_view(), name='show_author'),

]