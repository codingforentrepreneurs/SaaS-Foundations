from django.contrib import admin

# Register your models here.
from .models import Subscription, UserSubscription

admin.site.register(Subscription)


admin.site.register(UserSubscription)