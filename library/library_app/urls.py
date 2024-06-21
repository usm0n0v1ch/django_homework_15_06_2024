from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from library_app import views

urlpatterns=[
    path('',views.show_all,name='home'),
    path('categories/<int:pk>',views.category_show,name='categories'),
    path('authors/<int:pk>',views.author_show,name='authors'),
    path('author_add',views.author_add,name='author_add'),
    path('author_delete/<int:pk>', views.author_delete,name='author_delete'),
    path('author_edit/<int:pk>', views.author_edit,name='author_edit'),
    path('books/<int:pk>',views.book_show,name='books'),
    path('book_add',views.book_add,name='book_add'),
    path('book_delete/<int:pk>', views.book_delete,name='book_delete'),
    path('book_edit/<int:pk>', views.book_edit,name='book_edit'),
    path('category_add/',views.category_add,name='category_add'),
    path('category_edit/<int:pk>',views.category_edit,name='category_edit'),
    path('category_delete/<int:pk>',views.category_delete,name='category_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)