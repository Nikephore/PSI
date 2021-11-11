from django.db import models
from django.db.models.fields.related import ForeignKey
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Requerida para las instancias de libros únicos
import uuid
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


    def get_absolute_url(self):
        return slugify(self.first_name+" "+self.last_name+" "+self.pk)


class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    path_to_cover_image = models.FilePathField()
    number_copies_stock = models.IntegerField()
    date = models.DateField(null=True)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    slug = models.SlugField()
    author = models.ManyToManyField(Author, help_text="Introduzca un autor para este libro")


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug=slugify(self.pk)
        super(Book, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True)
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.msg





