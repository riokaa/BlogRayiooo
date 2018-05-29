from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    id = models.AutoField(primary_key=True, unique=True)


class ArticleType(models.Model):
    type = models.CharField(primary_key=True, unique=True, max_length=10)


class Article(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.ForeignKey(ArticleType, on_delete=models.PROTECT)
    content = models.TextField()
    timestamp = models.DateTimeField()
    click = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)

