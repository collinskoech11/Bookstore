from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BookList.as_view()),
    path('books/new', views.BookCreate.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view()),
    path('books/edit/<int:pk>', views.BookEdit.as_view()),#pending
    path('books/updatequantity/<int:pk>', views.BookStockUpdate.as_view()),#pending
    path('books/author/<int:pk>', views.AuthorBookList.as_view()),
    path('books/year/<int:pk>', views.YearBookList.as_view()),
    path('authors', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
    path('authors/new', views.AuthorCreate.as_view()),
    path('authors/edit/<int:pk>', views.AuthorEdit.as_view()),
]
