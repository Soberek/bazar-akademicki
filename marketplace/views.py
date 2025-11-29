from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Listing, Category, ListingImage
from .forms import ListingForm, ListingEditForm, ListingImageFormSet


def listing_list(request):
    """Lista wszystkich aktywnych ofert."""
    listings = Listing.objects.filter(status=Listing.Status.ACTIVE).select_related('seller', 'category')
    categories = Category.objects.filter(parent__isnull=True)
    
    # Filtrowanie
    category_slug = request.GET.get('category')
    if category_slug:
        listings = listings.filter(category__slug=category_slug)
    
    min_price = request.GET.get('min_price')
    if min_price:
        listings = listings.filter(price__gte=min_price)
    
    max_price = request.GET.get('max_price')
    if max_price:
        listings = listings.filter(price__lte=max_price)
    
    condition = request.GET.get('condition')
    if condition:
        listings = listings.filter(condition=condition)
    
    # Sortowanie
    sort = request.GET.get('sort', '-created_at')
    if sort in ['price', '-price', 'created_at', '-created_at', 'title']:
        listings = listings.order_by(sort)
    
    # Paginacja
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    
    return render(request, 'marketplace/listing_list.html', {
        'listings': listings,
        'categories': categories,
        'conditions': Listing.Condition.choices,
    })


def listing_detail(request, pk):
    """Szczegóły pojedynczej oferty."""
    listing = get_object_or_404(
        Listing.objects.select_related('seller', 'category').prefetch_related('images'),
        pk=pk
    )
    
    # Zwiększ licznik wyświetleń
    listing.views_count += 1
    listing.save(update_fields=['views_count'])
    
    # Podobne oferty
    similar_listings = Listing.objects.filter(
        category=listing.category,
        status=Listing.Status.ACTIVE
    ).exclude(pk=pk)[:4]
    
    return render(request, 'marketplace/listing_detail.html', {
        'listing': listing,
        'similar_listings': similar_listings,
    })


@login_required
def listing_create(request):
    """Tworzenie nowej oferty."""
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            
            # Obsługa zdjęć
            images = request.FILES.getlist('images')
            for i, image in enumerate(images):
                ListingImage.objects.create(
                    listing=listing,
                    image=image,
                    is_main=(i == 0)  # Pierwsze zdjęcie jako główne
                )
            
            messages.success(request, 'Oferta została dodana!')
            return redirect('marketplace:listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
    
    return render(request, 'marketplace/listing_create.html', {
        'form': form,
        'categories': Category.objects.all(),
    })


@login_required
def listing_edit(request, pk):
    """Edycja oferty."""
    listing = get_object_or_404(Listing, pk=pk)
    
    # Sprawdź czy użytkownik jest właścicielem
    if listing.seller != request.user:
        messages.error(request, 'Nie masz uprawnień do edycji tej oferty.')
        return redirect('marketplace:listing_detail', pk=pk)
    
    if request.method == 'POST':
        form = ListingEditForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            
            # Obsługa nowych zdjęć
            images = request.FILES.getlist('images')
            for image in images:
                ListingImage.objects.create(listing=listing, image=image)
            
            messages.success(request, 'Oferta została zaktualizowana!')
            return redirect('marketplace:listing_detail', pk=listing.pk)
    else:
        form = ListingEditForm(instance=listing)
    
    return render(request, 'marketplace/listing_edit.html', {
        'form': form,
        'listing': listing,
    })


@login_required
def listing_delete(request, pk):
    """Usuwanie oferty."""
    listing = get_object_or_404(Listing, pk=pk)
    
    # Sprawdź czy użytkownik jest właścicielem
    if listing.seller != request.user:
        messages.error(request, 'Nie masz uprawnień do usunięcia tej oferty.')
        return redirect('marketplace:listing_detail', pk=pk)
    
    if request.method == 'POST':
        listing.delete()
        messages.success(request, 'Oferta została usunięta.')
        return redirect('marketplace:listing_list')
    
    return render(request, 'marketplace/listing_delete.html', {
        'listing': listing,
    })


def category_detail(request, slug):
    """Lista ofert w danej kategorii."""
    category = get_object_or_404(Category, slug=slug)
    listings = Listing.objects.filter(
        category=category,
        status=Listing.Status.ACTIVE
    ).select_related('seller')
    
    # Paginacja
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    
    return render(request, 'marketplace/category_detail.html', {
        'category': category,
        'listings': listings,
    })


def search(request):
    """Wyszukiwanie ofert."""
    query = request.GET.get('q', '')
    listings = Listing.objects.filter(status=Listing.Status.ACTIVE)
    
    if query:
        listings = listings.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    
    # Filtrowanie
    category_slug = request.GET.get('category')
    if category_slug:
        listings = listings.filter(category__slug=category_slug)
    
    min_price = request.GET.get('min_price')
    if min_price:
        listings = listings.filter(price__gte=min_price)
    
    max_price = request.GET.get('max_price')
    if max_price:
        listings = listings.filter(price__lte=max_price)
    
    # Sortowanie
    sort = request.GET.get('sort', '-created_at')
    if sort in ['price', '-price', 'created_at', '-created_at']:
        listings = listings.order_by(sort)
    
    # Paginacja
    paginator = Paginator(listings, 12)
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    
    return render(request, 'marketplace/search.html', {
        'listings': listings,
        'query': query,
        'categories': Category.objects.all(),
    })
