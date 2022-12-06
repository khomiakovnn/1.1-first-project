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
    dates = list(set([str(b.pub_date) for b in Book.objects.all()]))
    dates.sort()
    if dates.index(pub_date) == len(dates)-1:
        date_before = dates[dates.index(pub_date)-1]
        date_after = dates[0]
    else:
        date_before = dates[dates.index(pub_date)-1]
        date_after = dates[dates.index(pub_date)+1]
    books = [{"name": b.name, "author": b.author, "pub_date": b.pub_date} for b in Book.objects.filter(pub_date=pub_date)]
    context = {'books': books,
               'date': pub_date,
               'date_before': date_before,
               'date_after': date_after,
    }
    return render(request, template, context)
