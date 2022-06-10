# pylint: disable=no-member
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
# Requerida para las instancias de libros únicos
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return slugify(self.first_name + " " + self.last_name + " " + str(self.pk))


class Book(models.Model):
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', unique=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    path_to_cover_image = models.FilePathField(auto_created=True)
    number_copies_stock = models.IntegerField()
    score = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    n_votes = models.IntegerField(default=0)
    date = models.DateField(null=True)
    slug = models.SlugField()
    author = models.ManyToManyField(Author, help_text="Introduzca un autor para este libro")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Para permitir titulos de libros repetidos
        super().save(*args, **kwargs)
        self.slug = slugify(self.title + ' ' + str(self.pk))
        super().save(update_fields=['slug'])

    def get_score(self):
        ret = 0
        if self.scores.all().count() > 0:
            for score in self.scores.all():
                ret += Decimal(score.rate)
            ret = ret / Decimal(self.scores.all().count())
            return str(round(ret, 2))
        return 'None'

    def update_score(self):
        avrg = self.get_score()
        if(avrg != 'None'):
            self.score = Decimal(avrg)
        else:
            self.score = 0
        self.n_votes = self.scores.all().count()
        super().save(update_fields=['score','n_votes'])

    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.slug)])


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True)
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.msg

class Vote(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='scores')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rate = models.IntegerField()
    ## validators=[MaxValueValidator(int('10')), MinValueValidator(int('0'))]

    def create_rate(book, user, rate):
        #Algo asi deberia funcionar
        #Pero hace falta probarlo para saber bien si no se pisan valoraciones 
        if(Vote.objects.all().count() > 0):
            ret, updated = Vote.objects.all().update_or_create(book=book, user=user, defaults={'rate' : str(rate)})
        else :
            v = Vote(book=book, user=user, rate=rate)
            v.save()
            ret = v
        book.update_score()
        return ret
        
    def __str__(self):
        return str(self.rate)

    