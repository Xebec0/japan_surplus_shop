from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from products.models import Product
from .models import Cart, CartItem, Order, OrderItem
from .forms import OrderCreateForm
from django.db.models import F

@login_required
def cart_detail(request):
    """
    View for displaying the shopping cart
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'orders/cart_detail.html', {'cart': cart})

@login_required
@require_POST
def cart_add(request, product_id):
    """
    View for adding a product to the shopping cart
    """
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    quantity = int(request.POST.get('quantity', 1))
    
    # Check if product is already in cart
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )
    
    # If product already exists in cart, update quantity
    if not item_created:
        cart_item.quantity = F('quantity') + quantity
        cart_item.save()
    
    messages.success(request, f'{product.name} added to your cart.')
    return redirect('orders:cart_detail')

@login_required
@require_POST
def cart_update(request, item_id):
    """
    View for updating the quantity of a product in the shopping cart
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    quantity = int(request.POST.get('quantity', 1))
    
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    
    messages.success(request, 'Cart updated successfully.')
    return redirect('orders:cart_detail')

@login_required
def cart_remove(request, item_id):
    """
    View for removing a product from the shopping cart
    """
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    
    messages.success(request, 'Item removed from cart.')
    return redirect('orders:cart_detail')

@login_required
def order_create(request):
    """
    View for creating a new order
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if cart.items.count() == 0:
        messages.warning(request, 'Your cart is empty.')
        return redirect('products:product_list')
    
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = cart.total_price
            order.save()
            
            # Create order items from cart items
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    price=item.product.price,
                    quantity=item.quantity
                )
            
            # Clear the cart
            cart.items.all().delete()
            
            # Redirect to payment page
            return redirect('orders:payment', order_id=order.id)
    else:
        # Pre-fill form with user information
        initial_data = {
            'full_name': f"{request.user.first_name} {request.user.last_name}",
            'email': request.user.email,
            'phone': request.user.phone_number,
            'address': request.user.address,
            'city': request.user.city,
            'state': request.user.state,
            'postal_code': request.user.postal_code,
            'country': request.user.country,
        }
        form = OrderCreateForm(initial=initial_data)
    
    return render(request, 'orders/order_create.html', {
        'cart': cart,
        'form': form
    })

@login_required
def payment(request, order_id):
    """
    View for handling payment
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    if request.method == 'POST':
        # Process payment (this would integrate with payment gateway)
        # For now, just mark as paid
        order.payment_completed = True
        order.status = 'processing'
        order.save()
        
        messages.success(request, 'Payment successful! Your order is being processed.')
        return redirect('orders:order_detail', order_id=order.id)
    
    return render(request, 'orders/payment.html', {'order': order})

@login_required
def order_detail(request, order_id):
    """
    View for displaying order details
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_list(request):
    """
    View for displaying all orders for a user
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})
