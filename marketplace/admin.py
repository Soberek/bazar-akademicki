from django.contrib import admin
from .models import Category, Listing, ListingImage


class ListingImageInline(admin.TabularInline):
    """Inline dla zdjęć oferty."""
    model = ListingImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin dla kategorii."""
    list_display = ('name', 'slug', 'parent', 'created_at')
    list_filter = ('parent',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    """Admin dla ofert."""
    list_display = ('title', 'seller', 'category', 'price', 'status', 'condition', 'created_at')
    list_filter = ('status', 'condition', 'category', 'created_at')
    search_fields = ('title', 'description', 'seller__username')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('views_count', 'created_at', 'updated_at')
    inlines = [ListingImageInline]
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('title', 'slug', 'description', 'price')
        }),
        ('Kategoria i stan', {
            'fields': ('category', 'condition', 'status')
        }),
        ('Sprzedający', {
            'fields': ('seller', 'location')
        }),
        ('Statystyki', {
            'fields': ('views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    """Admin dla zdjęć ofert."""
    list_display = ('listing', 'is_main', 'created_at')
    list_filter = ('is_main',)
    search_fields = ('listing__title',)
