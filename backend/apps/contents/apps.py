from django.apps import AppConfig


class ContentConfig(AppConfig):
    name = 'apps.contents'

    def ready(self):
        import apps.contents.signals
