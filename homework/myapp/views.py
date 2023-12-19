from datetime import timedelta
from django.utils import timezone
from myapp.models import Customer, Order
from django.shortcuts import render
from django.views.generic import TemplateView
from typing import Any


timedelta()


def week():
    return timezone.now() - timedelta(days=7)


def month():
    return timezone.now() - timedelta(days=30)


def year():
    return timezone.now() - timedelta(days=365)


def get_tuple_products(query_set: Order):
    lst = []
    for order in query_set:
        for productt in order.product.all():
            lst.append(productt.name)
    return set(lst)


class TemplCustomers(TemplateView):
        template_name = 'myapp/users.html'

        def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['customers'] = Customer.objects.all()
            return context
        

class TemplateInfoAboutOrders(TemplateView):
    template_name = 'myapp/products_of_customer.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        orders = Order.objects.filter(customer=context['customer_id'], order_date__gte=month())
        context['day7'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], order_date__gte=week()))
        context['day30'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], order_date__gte=month()))
        context['day365'] = get_tuple_products(Order.objects.filter(customer=context['customer_id'], order_date__gte=year()))
        context['orders'] = orders

        return context