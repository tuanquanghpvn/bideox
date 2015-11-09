from django.apps import AppConfig

class UserAppConfig(AppConfig):
    name = 'apps.users'
    verbose_name = 'UserProfile'

    def ready(self):
        from apps.users import signals
