from django.apps import AppConfig


class KnowledgeBankConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "knowledge_bank"

    def ready(self):
        import knowledge_bank.signals
