from django.urls import path
from . import views
urlpatterns = [
	path('', views.books),
    path('authors', views.authors),
    path('authors_create', views.authors_create),
    path('authors/<int:authorID>', views.author_view),
    path('add_book_to_author/<int:authorID>', views.add_book_to_author),
    path('books_create', views.books_create),
    path('books/<int:bookID>', views.book_view),
    path('add_author_to_book/<int:bookID>', views.add_author_to_book),
]