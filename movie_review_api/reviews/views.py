from rest_framework import generics, filters
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['movie__title', 'rating']  # Allows filtering by movie title & rating

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
