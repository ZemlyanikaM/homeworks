from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Client, Product, Order
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)


def products(request):
    logger.info(f'products request received')
    products = Product.objects.all()
    res = ''
    for product in products:
        res += str(product)
    return HttpResponse(res)


def clients(request):
    logger.info(f'Clients request received')
    cls = Client.objects.all()
    res = ''
    for client in cls:
        res += str(client)

    return HttpResponse(res)


def orders(request):
    logger.info(f'Orders request received')
    orders = Order.objects.all()
    res = ''
    for order in orders:
        res += str(order)
    return HttpResponse(res)


def clients_sorted_products(request, id_client: int, days: int):
    # products = []
    products_set = []
    now = datetime.now()
    before = now - timedelta(days=days)
    client = Client.objects.filter(pk=id_client).first()
    orders = Order.objects.filter(customer=client, date_create_order__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in products_set:
                products_set.append(product)

    return render(request, 'hw3app/clients_sorted_products.html',
                  {'client': client, 'products_set': products_set, 'days': days})
