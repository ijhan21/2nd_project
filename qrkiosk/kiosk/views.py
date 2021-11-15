from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.db.models import Q
import collections
from itertools import combinations

# Create your views here.

#http://localhost:8000/?company=1&&table=2
def store(request, table):
    table =Table.objects.get(id=table)
    company = table.company
    products= Product.objects.filter(company=company)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    cartItems = order.get_cart_items
    context={'products':products, 'cartItems':cartItems, 'table':table, 'company':company}
    return render(request, 'store/store.html', context)

def search(request):
    company_id=request.GET.get('company')
    table_id=request.GET.get('table')
    # company_id, table_id = 1,3
    company =Company.objects.get(id=company_id) # '목동점 id
    table =Table.objects.get(name=table_id, company=company_id)
    products= Product.objects.filter(company=company)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    cartItems = order.get_cart_items
    context={'products':products, 'cartItems':cartItems, 'table':table, 'company':company}
    return render(request, 'store/store.html', context)

def cart(request, table):
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
    context = {'items':items, 'order':order, 'cartItems':cartItems, 'table':table}
    return render(request, 'store/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    table = data['table']
    table =Table.objects.get(id=table) 
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
    table = Table.objects.get(id=table)
    orders = table.order_set.all()
    
    for order in orders:
        order.order_complete=True
        order.save()
    context={}
    return render(request, 'store/thanks.html', context)

###############################################################################################
########## 주인장 view#########################################################################
###############################################################################################
## http://localhost:8000/manage/?company=1
def manage(request):
    company_id=request.GET.get('company')        
    company =Company.objects.get(id=company_id) # '목동점 id
    tables = company.table_set.all()
    datas = dict()
    for table in tables:
        datas[table]=[]
        orders = table.order_set.filter(serve_complete=False, order_complete=True)   
        for order in orders:
            items = order.orderitem_set.all()
            for item in items:
                datas[table].append(item)
    # 내용이 없으면 빼기
    order_data=dict()
    for key, value in datas.items():        
        if value:
           order_data[key]=value

    context={'order_data':order_data, 'company':company}
    return render(request, 'store/manage.html', context)

def update_serve(request):
    data = json.loads(request.body)
    table_id = data['key']
    action = data['action']
    orders = Order.objects.filter(table=table_id)
    for order in orders:
        order.serve_complete = True
        order.save()
    return JsonResponse('Item was Fully added', safe=False)

def summary(request, table=None):        
    # company = Company.objects.get_or_create(id=5)
    ml_counter=list()
    tables= Table.objects.filter(company=5)
    for table in tables:
        orders= Order.objects.filter(table=table, serve_complete=True)
        for order in orders:
            temp_combination=list()
            orderItems = OrderItem.objects.filter(order=order)
            for orderItem in orderItems:
                temp_combination.append(orderItem.product)
            if len(temp_combination)>1:
                ml_counter+=list(combinations(temp_combination,2))
    ml = collections.Counter(ml_counter)
    suggest_datas = ml.most_common(3)
    suggest_items = [dt[0] for dt in suggest_datas]
    context={'suggest_items':suggest_items}
    return render(request, 'store/summary.html', context)