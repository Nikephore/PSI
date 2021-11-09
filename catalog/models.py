from django.db import models
from django.db.models.fields.related import ForeignKey
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Requerida para las instancias de libros únicos
import uuid
from django.contrib.auth.models import User
from datetime import date


class Author(models.Model):
    author_id = models.IntegerField(primary_key= True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    book_id = models.IntegerField(primary_key= True)
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=200)
    price = models.DecimalField()
    path_to_cover_image = models.FilePathField()
    number_of_copies_stock = models.IntegerField()
    date = models.DateField()
    score = models.DecimalField()
    slug = models.SlugField()

class AuthorBook(models.Model): 
    book_id = ForeignKey(Book, on_delete=models.SET_NULL)
    author_id = ForeignKey(Author, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('book_id', 'author_id')



class Comment(models.Model):
    comment_id = models.IntegerField(primary_key= True)
    book_id = ForeignKey(Book, on_delete=models.SET_NULL)
    user_id = ForeignKey(Book, on_delete=models.SET_NULL)
    date = models.DateField()
    msg = models.CharField(max_length=500)





