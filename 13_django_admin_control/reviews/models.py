from django.db import models
from django.utils import timezone

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    product_name = models.CharField(max_length=200)
    review_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    author = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.product_name} - {self.rating} stars"

    class Meta:
        ordering = ['-created_at']
