from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book, name="book"),
    re_path(r'^book/([0-9]+)/edit$', views.rate_apply, name="edit_book"),
    re_path(r'^home/(?P<Id>[0-9]+)/$',views.home, name='home'),
    # re_path(r'^author/$', views.all_writer_view),
]