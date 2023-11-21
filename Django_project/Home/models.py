from django.db import models

class ProcessedImage(models.Model):
    original_image = models.ImageField(upload_to='original_images/',null=True, blank=True)
    processed_image = models.ImageField(upload_to='processed_images/')
