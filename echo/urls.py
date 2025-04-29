from django.urls import path
 
from .views import book_list, book_detail, book_edit, book_delete, book_new


urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('book/new/', book_new, name='book_new'),
    path('book/<int:pk>/edit/', book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', book_delete, name='book_delete'),    
]

