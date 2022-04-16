from django.apps import AppConfig


class MessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'message'

    def ready(self):
        # noinspection PyUnresolvedReferences
        from . import signals