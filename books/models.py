import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

# python manage.py shell


class Author(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateTimeField('date published')


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateTimeField('date published')

    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title