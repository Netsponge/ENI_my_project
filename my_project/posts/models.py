
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=75)
    models.EmailField((""), max_length=254) = models.TextField()
    password = models.CharField(max_length=75)

    def __str__(self):
        return self.title
