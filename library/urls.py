from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'library'
urlpatterns = [
    path('bookapi/', views.BooksView.as_view(), name='Books-list'),
    path('bookapi/<int:pk>', views.BookView.as_view(), name='Book-detail'),
    path('authorapi/', views.AuthorsView.as_view(), name='Author-list'),
    path('authorapi/<int:pk>', views.AuthorView.as_view(), name='Author-detail'),
    path('api/', views.api_root, name='api-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)