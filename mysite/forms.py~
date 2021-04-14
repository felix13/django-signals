from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    pages = forms.CharField(max_length=50)

    class Meta:
        model = Book
        fields = ['name', 'pages']
