from django.core.paginator import Paginator
from django.shortcuts import render
from books.models import Book
from datetime import datetime, timedelta


def books_view(request):
    template = "books/books_list.html"
    books = Book.objects.all().order_by("pub_date")
    context = {"books": books}
    return render(request, template, context)


def book_page(request, pub_date):
    template = "books/books_list.html"
    books = Book.objects.filter(pub_date__exact=pub_date)
    previous_page = Book.objects.filter(pub_date__lt=pub_date).first()
    next_page = Book.objects.filter(pub_date__gt=pub_date).first()

    context = {"books": books, "previous_page": previous_page, "next_page": next_page}
    return render(request, template, context)
