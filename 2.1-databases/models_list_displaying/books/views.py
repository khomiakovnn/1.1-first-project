from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = [{"name": b.name, "author": b.author, "pub_date": b.pub_date} for b in Book.objects.all()]
    context = {'books': books}
    return render(request, template, context)


def date_view(request, pub_date):
    template = 'books/books_pagi.html'
    CONTENT = [{"name": b.name, "author": b.author, "pub_date": b.pub_date} for b in Book.objects.all()]
    paginator = Paginator(CONTENT)
    page = paginator.get_page()
    context = {'books': books,
               'date': pub_date,
               'page': page,
    }
    return render(request, template, context)
