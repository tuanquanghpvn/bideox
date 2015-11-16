from rest_framework import serializers

from . import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
       model = models.Post 
       fields = ('id', 'name', 'slug', 'description', 'videoDurationFe',
                'externalView', 'dateCreate', 'category', 'profile')
