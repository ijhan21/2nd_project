from django.urls import path, include

from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('<int:table>/cart/', views.cart, name="cart_process"),
	path('<int:table>/checkout/', views.checkout, name="checkout"),
	
	path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),
	path('<int:table>/order_complete/', views.orderComplete, name='order_complete'),
    
]