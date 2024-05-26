from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'Masala Chai'),
        ('BL', 'Black Chai'),
        ('WL', 'White Chai'),
        ('SL', 'Sweet Chai'),
        ('CL', 'Coffee Chai'),
        ('GL', 'Green Chai'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES)
    description = models.TextField(default='')
    price = models.CharField(max_length=5, default='0')

    def __str__(self):
        return self.name
