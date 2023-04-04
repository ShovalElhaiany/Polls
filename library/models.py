from django.db import models
from django.core import validators


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(validators=[validators.EmailValidator])

    def __str__(self) -> str:
        return f'{self.first_name}{self.last_name}'


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    pub_date = models.DateTimeField('Date published')

    def __str__(self) -> str:
        return self.book_name
