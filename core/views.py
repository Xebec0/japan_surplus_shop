from django.shortcuts import render
from products.models import Product, Category
from django.views.generic import TemplateView

def home_view(request):
    """
    View for the home page
    """
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    categories = Category.objects.all()[:6]
    
    return render(request, 'core/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })

class AboutView(TemplateView):
    """
    View for the about page
    """
    template_name = 'core/about.html'

class ContactView(TemplateView):
    """
    View for the contact page
    """
    template_name = 'core/contact.html'

def error_404_view(request, exception):
    """
    View for 404 errors
    """
    return render(request, 'core/404.html', status=404)

def error_500_view(request):
    """
    View for 500 errors
    """
    return render(request, 'core/500.html', status=500)
