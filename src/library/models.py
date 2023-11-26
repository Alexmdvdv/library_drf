from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=100)
    year_publication = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)


