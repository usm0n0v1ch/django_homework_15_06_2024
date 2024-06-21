from django.shortcuts import render, get_object_or_404, redirect

from library_app.forms import CategoryForm, AuthorForm, BookForm
from library_app.models import Book, Category, Author


# Create your views here.

def show_all(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    authors = Author.objects.all()
    ctx = {
        'books': books,
        'categories': categories,
        'authors': authors
    }
    return render(request,'library_app/home.html', ctx)
def category_show(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = Book.objects.filter(category=category)
    ctx = {
        'category': category,
        'books': books
    }
    return render(request, 'library_app/categories.html', ctx)
def author_show(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    ctx = {
        'author': author,
        'books': books
    }
    return render(request, 'library_app/authors.html', ctx)

def book_show(request, pk):
    book = get_object_or_404(Book, pk=pk)
    ctx = {
        'book': book
    }
    return render(request, 'library_app/books.html', ctx)

def category_add(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    ctx = {
        'form':form
    }
    return render(request,'library_app/category_add.html',ctx)

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm(instance=category)

    ctx = {
        'form': form
    }
    return render(request, 'library_app/category_edit.html', ctx)
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category.delete()
        return redirect('home')

    ctx = {
        'category': category
    }
    return render(request, 'library_app/category_delete.html', ctx)






def author_add(request):
    if request.method=="POST":
        form = Author(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    ctx = {
        'form':form
    }
    return render(request,'library_app/author_add.html',ctx)

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()
        return redirect('home')

    ctx = {
        'author': author
    }
    return render(request, 'library_app/author_delete.html', ctx)
def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm(instance=author)

    ctx = {
        'form': form
    }
    return render(request, 'library_app/author_edit.html', ctx)



def book_add(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    ctx = {
        'form':form
    }
    return render(request,'library_app/book_add.html',ctx)


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    ctx = {
        'book': book
    }
    return render(request, 'library_app/book_delete.html', ctx)


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    ctx = {
        'form': form
    }
    return render(request, 'library_app/book_edit.html', ctx)