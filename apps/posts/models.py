from django.db import models

from apps.categories.models import Category

class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    videoDurationFe = models.CharField(max_length=255)
    externalView = models.IntegerField()
    dateCreate = models.DateTimeField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
