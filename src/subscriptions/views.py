from django.shortcuts import render

from subscriptions.models import SubscriptionPrice

# Create your views here.
def subscription_price_view(request):
    qs = SubscriptionPrice.objects.filter(featured=True)
    monthly_qs = qs.filter(interval=SubscriptionPrice.IntervalChoices.MONTHLY)
    year_qs = qs.filter(interval=SubscriptionPrice.IntervalChoices.MONTHLY)
    return render(request, "subscriptions/pricing.html", {
        "monthly_qs": monthly_qs,
        "year_qs": year_qs,
    })