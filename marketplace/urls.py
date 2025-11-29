from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    # Strona główna / lista ofert
    path('', views.listing_list, name='listing_list'),
    
    # Szczegóły oferty
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    
    # CRUD ofert
    path('listing/create/', views.listing_create, name='listing_create'),
    path('listing/<int:pk>/edit/', views.listing_edit, name='listing_edit'),
    path('listing/<int:pk>/delete/', views.listing_delete, name='listing_delete'),
    
    # Kategorie
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
    # Wyszukiwanie
    path('search/', views.search, name='search'),
]
