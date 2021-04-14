from django.apps import AppConfig


class MysiteConfig(AppConfig):
    name = 'mysite'
    verbose_name = "Mysite"
    
    def ready(self):
        import mysite.signals

        pass
