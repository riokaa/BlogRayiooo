from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=64)


class ArticleType(models.Model):
    type = models.CharField(primary_key=True, unique=True, max_length=10)


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.ForeignKey(ArticleType, on_delete=models.PROTECT)
    content = models.TextField()
    timestamp = models.DateTimeField()
    click = models.IntegerField(default=0)

