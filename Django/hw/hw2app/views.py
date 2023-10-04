from django.shortcuts import render
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
