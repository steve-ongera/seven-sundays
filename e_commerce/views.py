from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category, Brand, Review
from .forms import CustomUserCreationForm


def home_view(request):
    """Home page with featured products"""
    featured_products = Product.objects.filter(is_active=True, is_featured=True)[:8]
    categories = Category.objects.filter(is_active=True, parent=None)[:6]
    latest_products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    
    context = {
        'featured_products': featured_products,
        'categories': categories,
        'latest_products': latest_products,
    }
    return render(request, 'home.html', context)


def product_list_view(request):
    """Product listing page with filters"""
    products = Product.objects.filter(is_active=True)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Brand filter
    brand_slug = request.GET.get('brand')
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
    
    # Sorting
    sort_by = request.GET.get('sort', 'name')
    if sort_by == 'price_low':
        products = products.order_by('price')
    elif sort_by == 'price_high':
        products = products.order_by('-price')
    elif sort_by == 'newest':
        products = products.order_by('-created_at')
    else:
        products = products.order_by('name')
    
    # Pagination
    paginator = Paginator(products, 12)  # 12 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get categories and brands for filters
    categories = Category.objects.filter(is_active=True)
    brands = Brand.objects.filter(is_active=True)
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'brands': brands,
        'search_query': search_query,
        'current_category': category_slug,
        'current_brand': brand_slug,
        'current_sort': sort_by,
    }
    return render(request, 'product_list.html', context)


def product_detail_view(request, slug):
    """Product detail page with similar products"""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    
    # Get similar products (same category, excluding current product)
    similar_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(id=product.id)
    
    # Pagination for similar products
    paginator = Paginator(similar_products, 4)  # 4 similar products per page
    page_number = request.GET.get('page')
    similar_products_page = paginator.get_page(page_number)
    
    # Get product reviews
    reviews = Review.objects.filter(product=product, is_approved=True).order_by('-created_at')
    
    # Calculate average rating
    total_reviews = reviews.count()
    if total_reviews > 0:
        avg_rating = sum([review.rating for review in reviews]) / total_reviews
        avg_rating = round(avg_rating, 1)
    else:
        avg_rating = 0
    
    context = {
        'product': product,
        'similar_products_page': similar_products_page,
        'reviews': reviews,
        'total_reviews': total_reviews,
        'avg_rating': avg_rating,
    }
    return render(request, 'product_detail.html', context)


def category_view(request, slug):
    """Category page showing products in that category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    products = Product.objects.filter(category=category, is_active=True)
    
    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'category.html', context)


def register_view(request):
    """User registration"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)