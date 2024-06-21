from django import forms

from library_app.models import Category, Author, Book


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'