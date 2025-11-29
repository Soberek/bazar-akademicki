from django.urls import path
from . import api_views

app_name = 'marketplace_api'

urlpatterns = [
    path('listings/', api_views.ListingListAPIView.as_view(), name='listing_list'),
    path('listings/<int:pk>/', api_views.ListingDetailAPIView.as_view(), name='listing_detail'),
    path('categories/', api_views.CategoryListAPIView.as_view(), name='category_list'),
]
