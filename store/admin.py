from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Cart, Wishlist, Order, Contact, Rating

<<<<<<< HEAD
admin.site.site_header = "VOGUE STORE Admin"
admin.site.site_title = "VOGUE Admin"
admin.site.index_title = "Admin Panel"
=======

# ── Site-wide admin branding ───────────────────────────────────────────────────
admin.site.site_header  = "VOGUE STORE"
admin.site.site_title   = "Vogue Store Admin"
admin.site.index_title  = "🛍️  Store Management Dashboard"
>>>>>>> 9a081e2c9ea17dad4b66470b73a4b068771dbf8f


# ── Product ────────────────────────────────────────────────────────────────────
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display  = ('product_image', 'name', 'category_badge', 'formatted_price', 'star_rating')
    list_filter   = ('category',)
    search_fields = ('name',)
    list_editable = ('name',)
    ordering      = ('category', 'name')
    list_per_page = 20

    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'category', 'price')
        }),
        ('Media & Rating', {
            'fields': ('image', 'rating'),
            'classes': ('collapse',),
            'description': 'Upload a product image and set the default rating.'
        }),
    )

    def product_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width:50px;height:50px;object-fit:cover;'
                'border-radius:8px;border:2px solid #e91e8c;" />',
                obj.image.url
            )
        return format_html('<span style="color:#ccc;">No image</span>')
    product_image.short_description = 'Image'

    def formatted_price(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:700;">&#8377; {:,}</span>',
            obj.price
        )
    formatted_price.short_description = 'Price'
    formatted_price.admin_order_field = 'price'

    def category_badge(self, obj):
        colours = {'men': '#3498db', 'women': '#e91e8c', 'kids': '#f39c12'}
        colour  = colours.get(obj.category, '#888')
        return format_html(
            '<span style="background:{};color:#fff;padding:3px 10px;'
            'border-radius:12px;font-size:0.75rem;font-weight:600;">{}</span>',
            colour, obj.get_category_display()
        )
    category_badge.short_description = 'Category'
    category_badge.admin_order_field = 'category'

    def star_rating(self, obj):
        if obj.rating is None:
            return format_html('<span style="color:#ccc;">&#8212;</span>')
        stars = '&#9733;' * obj.rating + '&#9734;' * (5 - obj.rating)
        return format_html(
            '<span style="color:#f39c12;font-size:1rem;">{}</span>',
            stars
        )
    star_rating.short_description = 'Rating'


# ── Order ──────────────────────────────────────────────────────────────────────
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display    = ('order_id', 'name', 'email', 'product_name', 'city', 'state_badge', 'order_date')
    list_filter     = ('city', 'state', 'created_at')
    search_fields   = ('name', 'email', 'pincode', 'product__name')
    ordering        = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page   = 25
    date_hierarchy  = 'created_at'

    fieldsets = (
        ('Customer Details', {
            'fields': ('name', 'email')
        }),
        ('Delivery Address', {
            'fields': ('address', 'city', 'state', 'pincode')
        }),
        ('Order Info', {
            'fields': ('product', 'created_at')
        }),
    )

    def order_id(self, obj):
        return format_html(
            '<span style="background:#1a1a2e;color:#fff;padding:3px 8px;'
            'border-radius:6px;font-size:0.8rem;font-weight:700;">#{}</span>',
            obj.id
        )
    order_id.short_description = 'Order ID'
    order_id.admin_order_field = 'id'

    def product_name(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:600;">{}</span>',
            obj.product.name
        )
    product_name.short_description = 'Product'

    def state_badge(self, obj):
        return format_html(
            '<span style="background:#eee;color:#333;padding:2px 8px;'
            'border-radius:10px;font-size:0.78rem;">{}</span>',
            obj.state
        )
    state_badge.short_description = 'State'

    def order_date(self, obj):
        return obj.created_at.strftime('%d %b %Y, %I:%M %p')
    order_date.short_description = 'Ordered At'
    order_date.admin_order_field = 'created_at'


# ── Cart ───────────────────────────────────────────────────────────────────────
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display  = ('user', 'product_name', 'quantity', 'cart_total')
    list_filter   = ('user',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20

    def product_name(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:600;">{}</span>',
            obj.product.name
        )
    product_name.short_description = 'Product'

    def cart_total(self, obj):
        return format_html(
            '<strong style="color:#27ae60;">&#8377; {:,}</strong>',
            obj.total_price()
        )
    cart_total.short_description = 'Total'


# ── Wishlist ───────────────────────────────────────────────────────────────────
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display  = ('user', 'product_name', 'product_price')
    list_filter   = ('user',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20

    def product_name(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:600;">{}</span>',
            obj.product.name
        )
    product_name.short_description = 'Product'

    def product_price(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:700;">&#8377; {:,}</span>',
            obj.product.price
        )
    product_price.short_description = 'Price'


# ── Contact ────────────────────────────────────────────────────────────────────
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display    = ('name', 'email', 'short_message', 'received_at')
    search_fields   = ('name', 'email')
    ordering        = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page   = 20

    fieldsets = (
        ('Sender', {
            'fields': ('name', 'email', 'created_at')
        }),
        ('Message', {
            'fields': ('message',)
        }),
    )

    def short_message(self, obj):
        msg = obj.message[:60] + ('...' if len(obj.message) > 60 else '')
        return format_html('<span style="color:#555;">{}</span>', msg)
    short_message.short_description = 'Message Preview'

    def received_at(self, obj):
        return obj.created_at.strftime('%d %b %Y, %I:%M %p')
    received_at.short_description = 'Received At'
    received_at.admin_order_field = 'created_at'


# ── Rating ─────────────────────────────────────────────────────────────────────
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display  = ('user', 'product_name', 'star_display')
    list_filter   = ('stars',)
    search_fields = ('user__username', 'product__name')
    list_per_page = 20

    def product_name(self, obj):
        return format_html(
            '<span style="color:#e91e8c;font-weight:600;">{}</span>',
            obj.product.name
        )
    product_name.short_description = 'Product'

    def star_display(self, obj):
        filled = '&#9733;' * obj.stars
        empty  = '&#9734;' * (5 - obj.stars)
        return format_html(
            '<span style="color:#f39c12;font-size:1.1rem;">{}</span>'
            '<span style="color:#ccc;font-size:1.1rem;">{}</span>',
            filled, empty
        )
    star_display.short_description = 'Stars'
    star_display.admin_order_field = 'stars'
