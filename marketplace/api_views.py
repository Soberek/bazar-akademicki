from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Category
from .serializers import ListingSerializer, CategorySerializer


class ListingListAPIView(generics.ListCreateAPIView):
    """API endpoint dla listy ofert."""
    queryset = Listing.objects.filter(status=Listing.Status.ACTIVE)
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint dla szczegółów oferty."""
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryListAPIView(generics.ListAPIView):
    """API endpoint dla kategorii."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
