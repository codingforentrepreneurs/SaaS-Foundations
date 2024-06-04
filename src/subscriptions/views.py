from django.shortcuts import render
from django.urls import reverse

from subscriptions.models import SubscriptionPrice

# Create your views here.
def subscription_price_view(request, interval="month"):
    qs = SubscriptionPrice.objects.filter(featured=True)
    inv_mo = SubscriptionPrice.IntervalChoices.MONTHLY
    inv_yr = SubscriptionPrice.IntervalChoices.YEARLY
    object_list = qs.filter(interval=inv_mo)
    url_path_name = "pricing_interval"
    mo_url = reverse(url_path_name, kwargs={"interval": inv_mo})
    yr_url = reverse(url_path_name, kwargs={"interval": inv_yr})
    active = inv_mo
    if interval == inv_yr:
        active = inv_yr
        object_list = qs.filter(interval=inv_yr)
    return render(request, "subscriptions/pricing.html", {
        "object_list": object_list,
        "mo_url": mo_url,
        "yr_url": yr_url,
        "active": active,
    })