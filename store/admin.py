from django.contrib import admin
from .models import Product, Cart, Wishlist, Order, Contact, Rating

admin.site.site_header = "VOGUE STORE Admin"
admin.site.site_title = "VOGUE Admin"
admin.site.index_title = "Admin Panel"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'rating')
    list_filter = ('category',)
    search_fields = ('name',)
    list_editable = ('price', 'rating')
    ordering = ('category', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'product', 'city', 'state', 'created_at')
    list_filter = ('city', 'state', 'created_at')
    search_fields = ('name', 'email', 'pincode')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user',)


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    list_filter = ('user',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'stars')
