from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index),
    path('contact/', views.contact, name='contact'),
    path('product-cart/', views.product_cart, name='product_cart'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout_cart, name='checkout_cart'),
    path('checkout/<int:id>/', views.checkout, name='checkout'),
    path('product-list/', views.product_list, name='product_list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('add-to-wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('increase/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove/<int:id>/', views.remove_cart_item, name='remove_cart'),
    path('wishlist/remove/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/move-to-cart/<int:wishlist_id>/', views.move_to_cart, name='move_to_cart'),
    path('wishlist-to-cart/<int:id>/', views.wishlist_to_cart, name='wishlist_to_cart'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-history/', views.order_history, name='order_history'),
    path('success/', views.success, name='success'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('rate/<int:product_id>/', views.submit_rating, name='submit_rating')

]
