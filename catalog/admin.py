from django.contrib import admin

from .models import Author, Book, Comment


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    inlines = [BooksInline]


admin.site.register(Author, AuthorAdmin)


class CommentsInline(admin.TabularInline):
    model = Comment
    extra = 0


class AuthorsInLine(admin.TabularInline):
    model = Author
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn' )
    inLines = [AuthorsInLine, CommentsInline]


admin.site.register(Book, BookAdmin)


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, CommentAdmin)
