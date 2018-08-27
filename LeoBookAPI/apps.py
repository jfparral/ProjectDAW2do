from django.apps import AppConfig


class LeobookConfig(AppConfig):
    name = 'LeoBook'

    def ready(self):
        import LeoBookAPI.signals