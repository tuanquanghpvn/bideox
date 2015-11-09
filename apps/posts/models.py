from django.db import models

from apps.users.models import UserProfile
from apps.categories.models import Category

class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, default='')
    videoDurationFe = models.CharField(max_length=255)
    externalView = models.IntegerField(default=0)
    dateCreate = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    profile = models.ForeignKey(UserProfile, default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        db_table = 'post'
