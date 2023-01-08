from django.contrib import admin
from .models import Book, Order, Publisher, Author


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','gender', 'email')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'price', 'book_available')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'created')


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)