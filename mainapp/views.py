""" Mainapp views here
"""
from decimal import Decimal
from django.db.models import F, OuterRef, Subquery
from django.shortcuts import render

from .models import OrderHeader, OrderItem


def index_view(request):
    """ main view
    """
    costly = OrderItem.objects.filter(order=OuterRef('pk')).annotate(cost=F('price') * F('amount')).order_by('-cost')[:1]
    items_pk = [el.item_pk for el in OrderHeader.objects.annotate(item_pk=Subquery(costly.values('pk')))]
    items = OrderItem.objects.filter(pk__in=items_pk).select_related().annotate(cost=F('price') * F('amount'))
    prices, amounts = tuple(zip(*tuple(items.values_list('price', 'amount'))))

    # prepare relative chart values
    def chart_values(value_list, axis_range=10):
        chart_floor = min(value_list) * Decimal('0.9')
        chart_range = max(value_list) * Decimal('1.1') - chart_floor
        return tuple(
            zip(
                range(2, 40, 4),
                map(lambda x: '{:.3f}'.format(
                    (1 - (x - chart_floor) / chart_range) * axis_range
                ).replace(',', '.'), value_list)
            )
        )

    context = {
        'items': items,
        'chart_prices': chart_values(prices),
        'chart_amounts': chart_values(amounts),
    }
    return render(request, 'mainapp/index.html', context)


def empty_view(request):
    pass