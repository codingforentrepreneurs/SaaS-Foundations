from django.db import models

# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        permissions = [
            ("advanced", "Advanced Perm"), # subscriptions.advanced
            ("pro", "Pro Perm"),  # subscriptions.pro
            ("basic", "Basic Perm"),  # subscriptions.basic,
            ("basic_ai", "Basic AI Perm")
        ]