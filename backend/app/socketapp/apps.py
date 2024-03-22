from django.apps import AppConfig

class SocketappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'socketapp'

    def ready(self):
        from valueUpdater import updater
        updater.start()
