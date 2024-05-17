from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model): 
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.email}'
    