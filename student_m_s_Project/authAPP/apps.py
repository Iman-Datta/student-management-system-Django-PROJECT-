from django.apps import AppConfig

class AuthappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authAPP'

    def ready(self):
        import authAPP.signals  # <-- this line ensures signals are registered