""" Mainapp views here
"""
from django.db.models import F, OuterRef, Subquery
from django.shortcuts import render

from .models import OrderHeader, OrderItem


def index_view(request):
    """ main view
    """
    costly = OrderItem.objects.filter(order=OuterRef('pk')).annotate(cost=F('price') * F('amount')).order_by('-cost')[:1]
    items_pk = [el.item_pk for el in OrderHeader.objects.annotate(item_pk=Subquery(costly.values('pk')))]
    items = OrderItem.objects.filter(pk__in=items_pk).select_related().annotate(cost=F('price') * F('amount'))
    context = {'items': items}
    return render(request, 'mainapp/index.html', context)
