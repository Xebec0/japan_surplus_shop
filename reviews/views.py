from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from .models import Review
from .forms import ReviewForm

# Create your views here.

@login_required
def add_review(request, product_id):
    """
    View for adding a review to a product
    """
    product = get_object_or_404(Product, id=product_id)
    
    # Check if user has already reviewed this product
    existing_review = Review.objects.filter(product=product, user=request.user).first()
    
    if existing_review:
        messages.warning(request, 'You have already reviewed this product. You can edit your review below.')
        return redirect('reviews:edit_review', review_id=existing_review.id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            
            messages.success(request, 'Your review has been added successfully.')
            return redirect('products:product_detail', slug=product.slug)
    else:
        form = ReviewForm()
    
    return render(request, 'reviews/review_form.html', {
        'form': form,
        'product': product,
        'action': 'Add'
    })

@login_required
def edit_review(request, review_id):
    """
    View for editing an existing review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Your review has been updated successfully.')
            return redirect('products:product_detail', slug=review.product.slug)
    else:
        form = ReviewForm(instance=review)
    
    return render(request, 'reviews/review_form.html', {
        'form': form,
        'product': review.product,
        'action': 'Edit'
    })

@login_required
def delete_review(request, review_id):
    """
    View for deleting a review
    """
    review = get_object_or_404(Review, id=review_id, user=request.user)
    product = review.product
    
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect('products:product_detail', slug=product.slug)
    
    return render(request, 'reviews/delete_review.html', {
        'review': review,
        'product': product
    })
