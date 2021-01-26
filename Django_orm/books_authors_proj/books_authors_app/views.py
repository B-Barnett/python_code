from django.shortcuts import render, HttpResponse, redirect
from .models import book, author

def authors(request):
    all_authors = author.objects.all()
    context = {
        "all_authors" : all_authors,
    }
    return render(request, "authors.html", context)

def authors_create(request):
    new_author = author.objects.create(first_name = request.POST['form_first_name'], last_name = request.POST['form_last_name'], notes = request.POST['form_notes'])
    return redirect("/authors")

def add_book_to_author(request, authorID):
    this_author = author.objects.get(id = request.POST['author_id'])
    this_book = book.objects.get(id = request.POST['select_book'])
    this_author.books.add(this_book)
    return redirect(f"/authors/{authorID}")

def author_view(request, authorID):
    author_to_show = author.objects.get(id = authorID)
    book_to_add = book.objects.all()
    print(author_to_show)
    context = {
        "author_to_show" : author_to_show,
        "book_to_add" : book_to_add,
    }
    return render(request, "authorview.html", context)


def books(request):
    all_books = book.objects.all()
    context = {
        "all_books" : all_books,
    }
    return render(request, "books.html", context)

def books_create(request):
    new_book = book.objects.create(title = request.POST['form_title'], description = request.POST['form_description'])
    return redirect("/")

def add_author_to_book(request, bookID):
    this_author = author.objects.get(id= request.POST['select_author'])
    this_book = book.objects.get(id= request.POST['book_id'])
    print(this_book)
    print(this_author)
    this_author.books.add(this_book)
    return redirect(f"/books/{bookID}")

def book_view(request, bookID):
    book_to_show = book.objects.get(id = bookID)
    author_to_add = author.objects.all()
    print(book_to_show)
    context = {
        "book_to_show" : book_to_show,
        "author_to_add" : author_to_add,
    }
    return render(request, "bookview.html", context)