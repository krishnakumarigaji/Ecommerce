from django.conf import settings
from django.core.mail import send_mail
from .models import Order, Contact, Cart, Product, Wishlist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from .models import Banner,CategoryImage



def get_cart_count(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).count()
    return 0


def index(request):
    banners = Banner.objects.filter(is_active=True)
    men_products = Product.objects.filter(category='men')
    women_products = Product.objects.filter(category='women')
    kids_products = Product.objects.filter(category='kids')

    # Category images
    cat_images = CategoryImage.objects.all()
    cat_dict = {c.category: c.image.url for c in cat_images}

    return render(request, 'index.html', {
        'banners': banners,
        'men_products': men_products,
        'women_products': women_products,
        'kids_products': kids_products,
        'cart_count': get_cart_count(request),
        'men_image': cat_dict.get('men', ''),
        'women_image': cat_dict.get('women', ''),
        'kids_image': cat_dict.get('kids', ''),
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')
    return render(request, 'contact.html', {'cart_count': get_cart_count(request)})


@login_required
def product_cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    grand_total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'product_cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'cart_count': cart_items.count(),
    })


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"'{product.name}' added to cart!")
    return redirect('product_cart')


@login_required
def increase_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('product_cart')


@login_required
def decrease_quantity(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('product_cart')


@login_required
def remove_cart_item(request, id):
    item = get_object_or_404(Cart, id=id, user=request.user)
    item.delete()
    return redirect('product_cart')


def checkout(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'checkout.html', {
        'product': product,
        'cart_count': get_cart_count(request),
    })


def checkout_cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product') if request.user.is_authenticated else []
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'cart_count': get_cart_count(request),
    })


def place_order(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        name = f"{first_name} {last_name}".strip()
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')

        if product_id:
            product = get_object_or_404(Product, id=product_id)
            Order.objects.create(
                product=product, name=name, email=email,
                address=address, city=city, state=state, pincode=pincode
            )
        else:
            # Cart checkout — create one order per cart item
            if request.user.is_authenticated:
                cart_items = Cart.objects.filter(user=request.user).select_related('product')
                for item in cart_items:
                    for _ in range(item.quantity):
                        Order.objects.create(
                            product=item.product, name=name, email=email,
                            address=address, city=city, state=state, pincode=pincode
                        )
                cart_items.delete()

        # Send confirmation email silently
        try:
            send_mail(
                subject='Order Confirmation — VOGUE STORE',
                message=f'Hello {name},\n\nYour order has been placed successfully!\n\nThank you for shopping with VOGUE STORE.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=True,
            )
        except Exception:
            pass

        messages.success(request, "Order placed successfully! Check your email for confirmation.")
        return redirect('success')

    return redirect('home')


def about(request):
    return render(request, 'about.html', {'cart_count': get_cart_count(request)})


def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    if query:
        products = products.filter(name__icontains=query)
    if category:
        products = products.filter(category=category)

    return render(request, 'product_list.html', {
        'products': products,
        'cart_count': get_cart_count(request),
    })


@login_required(login_url='login')
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
    return render(request, 'wishlist.html', {
        'wishlist_items': wishlist_items,
        'cart_count': get_cart_count(request),
    })


@login_required(login_url='login')
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    messages.success(request, f"'{product.name}' added to wishlist!")
    return redirect('wishlist')


def remove_from_wishlist(request, wishlist_id):
    item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
    item.delete()
    return redirect('wishlist')


def wishlist_to_cart(request, id):
    wishlist_item = get_object_or_404(Wishlist, id=id, user=request.user)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user, product=wishlist_item.product, defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    wishlist_item.delete()
    return redirect('product_cart')


def move_to_cart(request, wishlist_id):
    return wishlist_to_cart(request, wishlist_id)


@login_required
def order_history(request):
    orders = Order.objects.filter(email=request.user.email).order_by('-created_at')
    return render(request, 'order_history.html', {
        'orders': orders,
        'cart_count': get_cart_count(request),
    })


def success(request):
    return render(request, 'success.html', {'cart_count': get_cart_count(request)})


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, f"Welcome, {username}! Account created successfully.")
        return redirect('home')
    return render(request, 'registration/register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, "You've been logged out successfully.")
    return redirect('home')

@login_required
def submit_rating(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        stars = request.POST.get('stars')
        Rating.objects.update_or_create(
            user=request.user, product=product,
            defaults={'stars': stars}
        )
    return redirect('product_list')
