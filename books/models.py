import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Book(models.Models):
    title = models.CharField(max_length=200)
    num_pages = models.IntegerField(default=0)
    date_published = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.title

