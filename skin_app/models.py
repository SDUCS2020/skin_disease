from django.db import models
from django.utils import timezone


class SkinImage(models.Model):
    """Model to store uploaded skin images and prediction results"""
    image = models.ImageField(upload_to='skin_images/')
    uploaded_at = models.DateTimeField(default=timezone.now)
    prediction = models.CharField(max_length=100, blank=True, null=True)
    confidence = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"Image {self.id} - {self.prediction or 'No prediction'}"
