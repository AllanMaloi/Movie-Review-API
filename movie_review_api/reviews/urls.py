from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView, MovieReviewListView

urlpatterns = [
    path('', ReviewListCreateView.as_view(), name='review-list'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('movie/<int:movie_id>/', MovieReviewListView.as_view(), name='movie-reviews'),
]
