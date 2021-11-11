from django.urls import path

from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('<int:table>/store', views.store, name="store"),
	path('', views.search, name="search"),
	path('cart/', views.cart, name="cart"),
	path('<int:table>/cart/', views.cart, name="cart_process"),
	path('<int:table>/checkout/', views.checkout, name="checkout"),
	
	path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),
	path('<int:table>/order_complete/', views.orderComplete, name='order_complete'),

	path('board/', views.boardDo, name='board'),
    path('post/', views.postDo, name='post'),

    path('manage/', views.manage, name='manage'),

	
]