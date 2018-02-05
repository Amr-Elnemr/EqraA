from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book),
    re_path(r'^home/([0-9]+)/$',views.home),
    # re_path(r'^author/$', views.all_writer_view),
]