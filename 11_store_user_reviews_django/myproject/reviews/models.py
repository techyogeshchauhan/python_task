from django.db import models

class ProductReview(models.Model):
    product_name = models.CharField(max_length=255)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.product_name} - {self.rating}/5"
