from datetime import datetime
from django.db import models


class Category(models.Model):

    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField('曜日', max_length=255)
    text = models.CharField('時間', max_length=255)
    sub = models.CharField('科目名', max_length=255)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', null=True)

    def __str__(self):
        return self.title
