from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book),
    re_path(r'^home/(?P<Id>[0-9]+)/$',views.home, name='home'),
    path('search/',views.search, name='search'),
    path('categories/',views.categories),
    # re_path(r'^author/$', views.all_writer_view),
]