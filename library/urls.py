from django.urls import path, re_path
from . import views

app_name = 'library'

urlpatterns = [
    re_path(r'^book/([0-9]+)/$', views.book, name="book"),
    re_path(r'^book/([0-9]+)/edit$', views.rate_apply, name="edit_book"),
    re_path(r'advanced_search', views.advanced_search, name="search"),
    re_path(r'search', views.search_all, name="search"),
    re_path(r'^category/(?P<Id>[0-9]+)/$',views.category,name='category'),
    re_path(r'^category/([0-9]+)/fav$', views.add_to_favorit, name="favorite_cat"),
    path('home/',views.home, name='home'),
    path('search/',views.search, name='search'),
    path('categories/',views.categories),
    path('author/<int:pk>/', views.show_author.as_view(), name='show_author'),

    re_path(r'^register/$', views.UserFormView.as_view(), name='register'),
    re_path(r'^login/$', views.loginform.as_view(), name='login'),
    
    re_path(r'^profile_page/$', views.ProfileView.as_view(), name='profile'),
    re_path(r'^edit_profile/$', views.edit_profile),
    re_path(r'^edit_profile_image/$', views.update_profile_image),

]