from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.db.models import Q
# Create your views here.
def store(request):
    company =Company.objects.get(id=1) # 'QR목동'점 id
    # print("company : ",company)
    table =Table.objects.get(id=1)
    products= Product.objects.filter(company=company)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    cartItems = order.get_cart_items
    context={'products':products, 'cartItems':cartItems, 'table':table, 'company':company}
    return render(request, 'store/store.html', context)

def cart(request, table=2):
    # company =Company.objects.get(id=1) 
    table =Table.objects.get(id=table)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context={'order':order, "items":items, "table":table, 'cartItems':cartItems}
    return render(request, 'store/cart.html', context)

def checkout(request, table):
    order, created = Order.objects.get_or_create(table=table, order_complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    print(cartItems)
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'table':table}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    table = data['table']
    table =Table.objects.get(id=table)
    print('Action~~:', action)
    print('ProductId:', productId)
    print("data",data)
    print("table",table, type(table))

    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(table=table, order_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity+1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity-1)
    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was Fully added', safe=False)

def processOrder(request):
    return JsonResponse('Payment complete', safe=False)

def orderComplete(request, table):
    # print('table:',table)
    table = Table.objects.get(id=table)
    orders = table.order_set.all()
    
    for order in orders:
        order.order_complete=True
        order.save()
        print("orders:",ord)
    return HttpResponseRedirect('/')
