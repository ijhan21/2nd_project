from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import datetime
from django.db.models import Q

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
    # print("company : ",company)
    table =Table.objects.get(name=table_id, company=company_id)
    print('table:', table)
    products= Product.objects.filter(company=company)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    cartItems = order.get_cart_items
    context={'products':products, 'cartItems':cartItems, 'table':table, 'company':company}
    return render(request, 'store/store.html', context)

<<<<<<< HEAD
def cart(request, table=2):
=======
def cart(request, table):
>>>>>>> companytable
    # company =Company.objects.get(id=1) 
    table =Table.objects.get(id=table)
    order,created= Order.objects.get_or_create(table=table, order_complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    print(order, table)
    print(order.get_cart_total)
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
    order_data = dict()
    for table in tables:
        order_data[table.name]=[]
        orders = table.order_set.filter(serve_complete=False)    
        for order in orders:
            items = order.orderitem_set.all()
            for item in items:
                order_data[table.name].append(item)            

    context={'order_data':order_data}
    return render(request, 'store/manage.html', context)
    return



###############################################################################################
from django.shortcuts import render
from django.http import HttpResponseRedirect
from board_app.models import Board
from django.urls import reverse

def boardDo(request):
        print("********************************************")
        boards = {'boards': Board.objects.all()}
        print("******---------------------------------**")
        return render(request, 'store/list.html', boards)


def postDo(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('index'))

    else:
        return render(request, 'store/post.html')
