import helpers.billing
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.conf import settings

from subscriptions.models import SubscriptionPrice

BASE_URL = settings.BASE_URL
# Create your views here.
def product_price_redirect_view(request, price_id=None, *args, **kwargs):
    request.session['checkout_subscription_price_id'] = price_id
    return redirect("stripe-checkout-start")


@login_required
def checkout_redirect_view(request):
    checkout_subscription_price_id = request.session.get("checkout_subscription_price_id")
    try:
        obj = SubscriptionPrice.objects.get(id=checkout_subscription_price_id)
    except:
        obj = None
    if checkout_subscription_price_id is None or obj is None:
        return redirect("pricing")
    customer_stripe_id = request.user.customer.stripe_id
    success_url_path = reverse("stripe-checkout-end")
    pricing_url_path = reverse("pricing")
    success_url = f"{BASE_URL}{success_url_path}"
    cancel_url= f"{BASE_URL}{pricing_url_path}"
    price_stripe_id = obj.stripe_id
    url = helpers.billing.start_checkout_session(
        customer_stripe_id,
        success_url=success_url,
        cancel_url=cancel_url,
        price_stripe_id=price_stripe_id,
        raw=False

    )
    return redirect(url)


def checkout_finalize_view(request):
    session_id = request.GET.get('session_id')
    checkout_r = helpers.billing.get_checkout_session(session_id, raw=True)
    customer_id = checkout_r.customer
    sub_stripe_id = checkout_r.subscription
    sub_r = helpers.billing.get_subscription(sub_stripe_id, raw=True)
    sub_plan = sub_r.plan
    sub_plan_price_stripe_id = sub_plan.id
    price_qs = SubscriptionPrice.objects.filter(stripe_id=sub_plan_price_stripe_id)
    print(price_qs)
    # print(sub_r )
    context = {
        "subscription": sub_r,
        "checkout": checkout_r
    }

    return render(request, "checkout/success.html", context)