from django.apps import AppConfig

class CheckoutConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"  # Prevents migration issues
    name = "checkout"

    def ready(self):
        import checkout.signals  # Ensures signals are loaded
