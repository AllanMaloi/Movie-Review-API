from rest_framework import generics, filters
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie__title', 'rating']
    ordering_fields = ['rating', 'created_at']  
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 

class MovieReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Review.objects.filter(movie__id=movie_id)
    
class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

