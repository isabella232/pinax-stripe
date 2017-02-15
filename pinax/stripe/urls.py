from django.conf.urls import url
from django.contrib import admin

from .views import (
    InvoiceListView,

    PaymentMethodListView,
    PaymentMethodCreateView,
    PaymentMethodDeleteView,
    PaymentMethodUpdateView,

    SubscriptionListView,
    SubscriptionCreateView,
    SubscriptionDeleteView,
    SubscriptionUpdateView,

    Webhook,
)

admin.autodiscover()

urlpatterns = [

    url(r"^subscriptions/$", SubscriptionListView.as_view(), name="pinax_stripe_subscription_list"),
    url(r"^subscriptions/create/$", SubscriptionCreateView.as_view(), name="pinax_stripe_subscription_create"),
    url(r"^subscriptions/(?P<pk>\d+)/delete/$", SubscriptionDeleteView.as_view(), name="pinax_stripe_subscription_delete"),
    url(r"^subscriptions/(?P<pk>\d+)/update/$", SubscriptionUpdateView.as_view(), name="pinax_stripe_subscription_update"),

    url(r"^payment-methods/$", PaymentMethodListView.as_view(), name="pinax_stripe_payment_method_list"),
    url(r"^payment-methods/create/$", PaymentMethodCreateView.as_view(), name="pinax_stripe_payment_method_create"),
    url(r"^payment-methods/(?P<pk>\d+)/delete/$", PaymentMethodDeleteView.as_view(), name="pinax_stripe_payment_method_delete"),
    url(r"^payment-methods/(?P<pk>\d+)/update/$", PaymentMethodUpdateView.as_view(), name="pinax_stripe_payment_method_update"),

    url(r"^invoices/$", InvoiceListView.as_view(), name="pinax_stripe_invoice_list"),

    url(r"^webhook/$", Webhook.as_view(), name="pinax_stripe_webhook"),
]
