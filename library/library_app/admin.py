from django.contrib import admin

from library_app.models import Book, Category, Author

# Register your models here.


admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)