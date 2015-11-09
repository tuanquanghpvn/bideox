from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True, related_name='profile')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'
        db_table = 'user_profile'