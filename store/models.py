from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    rating = models.IntegerField(blank=True, null=True)

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.TextField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default="NA")
    pincode = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    def total_price(self):
        return self.product.price * self.quantity


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField()

    def __str__(self):
        return self.product.name


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    eyebrow = models.CharField(max_length=100, blank=True, help_text="Small text above title e.g. 'New Arrivals 2026'")
    title = models.CharField(max_length=200, blank=True, help_text="Use \\n for line break e.g. 'The New\\nFashion Collection'")
    subtitle = models.CharField(max_length=300, blank=True)
    btn1_text = models.CharField(max_length=50, blank=True, help_text="First button text e.g. 'Shop Now'")
    btn1_url = models.CharField(max_length=200, blank=True, default='/product-list/')
    btn2_text = models.CharField(max_length=50, blank=True, help_text="Second button text e.g. 'Women's Edit'")
    btn2_url = models.CharField(max_length=200, blank=True, default='/product-list/')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Lower number shows first")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Banner {self.id}"


class CategoryImage(models.Model):
    CATEGORY_CHOICES = (
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.category