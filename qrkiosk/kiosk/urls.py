from django.urls import path, include

from . import views

urlpatterns = [
    #Leave as empty string for base url
	path('<int:table>/store', views.store, name="store"),
	path('', views.search, name="search"),
	path('cart/', views.cart, name="cart"),
	path('<int:table>/cart/', views.cart, name="cart_process"),
	path('<int:table>/checkout/', views.checkout, name="checkout"),
	path('<int:table>/cart/manage/summary', views.summary, name='summary'),
	path('update_item/', views.updateItem, name='update_item'),
	path('manage/summary/', views.summary, name='summary'),
	path('<int:table>/manage/summary/', views.summary, name='summary'),
	path('process_order/', views.processOrder, name='process_order'),
	path('manage/', views.manage, name='manage'),
	path('update_serve/', views.update_serve, name='update_serve'),
	path('<int:table>/order_complete/', views.orderComplete, name='order_complete'),
    
]