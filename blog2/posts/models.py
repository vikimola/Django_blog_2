from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    date_published = models.DateTimeField(datetime.utcnow())
    body = models.CharField(max_length=10000000000000)
