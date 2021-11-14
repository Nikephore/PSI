# Populate database
# This file has to be placed within the
# catalog/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# that is, populate.py.
#
# execute python manage.py  populate
#
# use module Faker generator to generate data (https://zetcode.com/python/faker/)
import decimal
import os
import pathlib

from django.core.management.base import BaseCommand
from catalog.models import (Author, Book, Comment)
from django.contrib.auth.models import User
from faker import Faker
from django.utils import timezone
import random
import datetime
# define STATIC_PATH in settings.py
from bookshop.settings import STATIC_PATH
from PIL import Image, ImageDraw, ImageFont


FONTDIR = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

# The name of this class is not optional must be Command
# otherwise manage.py will not process it properly
#


class Command(BaseCommand):
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = """populate database
           """

    # def add_arguments(self, parser):

    # handle is another compulsory name, do not change it"
    # handle function will be executed by 'manage populate'
    def handle(self, *args, **kwargs):
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here
        if 'DYNO' in os.environ:
            self.font = \
                "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
        else:
            self.font = \
                "/usr/share/fonts/truetype/freefont/FreeMono.ttf"

        self.NUMBERUSERS = 20
        self.NUMBERBOOKS = 30
        self.NUMBERAUTHORS = 10
        self.MAXAUTHORSPERBOOK = 3
        self.NUMBERCOMMENTS = 40
        self.MAXCOPIESSTOCK = 30
        self.cleanDataBase()   # clean database
        # The faker.Faker() creates and initializes a faker generator,
        self.faker = Faker()
        self.user()
        self.author()
        self.book()
        self.comment()
        # check a variable that is unlikely been set out of heroku
        # as DYNO to decide which font directory should be used.
        # Be aware that your available fonts may be different
        # from the ones defined here

    def cleanDataBase(self):
        # delete all models stored (clean table)
        # in database
        # remove pass and ADD CODE HERE
        pass

    def user(self):
        " Insert users"
        for _ in range(self.NUMBERUSERS):
            fn = self.faker.first_name()
            ln = self.faker.last_name()
            email = self.faker.email()
            username = self.faker.name()
            password = self.faker.sha256()
            new_user = User(first_name=fn, last_name=ln, email=email, username=username, password=password)
            new_user.save()

    def author(self):
        " Insert authors"
        for _ in range(self.NUMBERAUTHORS):
            fn = self.faker.first_name()
            ln = self.faker.unique.last_name()
            new_author = Author(first_name=fn, last_name=ln)
            new_author.save()

    def cover(self, book):
        """create fake cover image.
           This function creates a very basic cover
           that show (partially),
           the primary key, title and author name"""

        img = Image.new('RGB', (200, 300), color=(73, 109, 137))
        # your font directory may be different
        fnt = ImageFont.truetype(
            self.font,
            28, encoding="unic")
        d = ImageDraw.Draw(img)
        d.text((10, 100), "PK %05d" % book.id, font=fnt, fill=(255, 255, 0))
        d.text((20, 150), book.title[:15], font=fnt, fill=(255, 255, 0))
        d.text((20, 200), "By %s" % str(
            book.author.all()[0])[:15], font=fnt, fill=(255, 255, 0))
        img.save(os.path.join(STATIC_PATH, book.path_to_cover_image))

    def book(self):
        " Insert books"
        # remove pass and ADD CODE HERE
        for _ in range(self.NUMBERBOOKS):
            t = self.faker.unique.word()
            isbn = self.faker.unique.numerify("#############")
            p = float(decimal.Decimal(random.randrange(100, 999))/100)
            # ptci = self.faker.unique.path
            c = self.faker.unique.random_int(self.MAXCOPIESSTOCK)
            d = self.faker.date()
            s = float(decimal.Decimal(random.randrange(100, 999))/100)
            sl = t  # al ser solo una palabra no se distingue
            path_string = "covers/" + sl + ".png"
            pth = pathlib.Path(path_string)
            new_book = Book(isbn=isbn, title=t, price=p, path_to_cover_image=pth, number_copies_stock=c, date=d, score=s, slug=t)
            new_book.save()
            new_book.author.add(Author.objects.order_by("?").first())
            self.cover(new_book)
            new_book.save()

    def comment(self):
        " Insert comments"
        # remove pass and ADD CODE HERE
        for _ in range(self.NUMBERCOMMENTS):
            user = User.objects.order_by("?").first()
            book = Book.objects.order_by("?").first()
            date = datetime.datetime.now(tz=timezone.utc)
            msg = self.faker.text(max_nb_chars=200)

            new_comment = Comment(user=user, book=book, date=date, msg=msg)
            new_comment.save()
