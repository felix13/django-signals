from django.shortcuts import render

from .forms import BookForm
from .models import Book


def home(request):

    all_books = Book.objects.all()

    return render(request, "mysite/all_books.html", {'books': all_books})


def add_book(request):
    form = BookForm()
    all_books = Book.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST)
        form.save()
        return render(request, "mysite/all_books.html", {'books': all_books})

    return render(request, "mysite/add_book_form.html", {'form': form})
