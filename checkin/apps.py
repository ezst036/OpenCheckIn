from django.apps import AppConfig

class CheckinConfig(AppConfig):
    name = 'checkin'

    def ready(self):
        import checkin.signals