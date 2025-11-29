from rest_framework import serializers
from .models import Listing, Category, ListingImage


class CategorySerializer(serializers.ModelSerializer):
    """Serializer dla kategorii."""
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'icon', 'parent']


class ListingImageSerializer(serializers.ModelSerializer):
    """Serializer dla zdjęć oferty."""
    
    class Meta:
        model = ListingImage
        fields = ['id', 'image', 'is_main']


class ListingSerializer(serializers.ModelSerializer):
    """Serializer dla ofert."""
    
    seller_name = serializers.CharField(source='seller.get_full_name_or_username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    images = ListingImageSerializer(many=True, read_only=True)
    condition_display = serializers.CharField(source='get_condition_display', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Listing
        fields = [
            'id', 'title', 'slug', 'description', 'price',
            'category', 'category_name', 'seller', 'seller_name',
            'condition', 'condition_display', 'status', 'status_display',
            'location', 'views_count', 'images',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['seller', 'views_count', 'slug']
