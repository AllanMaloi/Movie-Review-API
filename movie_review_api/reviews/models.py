from django.db import models
from django.conf import settings
from movies.models import Movie

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie.title} - {self.rating}/5'
