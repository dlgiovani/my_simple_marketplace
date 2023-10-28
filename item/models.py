from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)
    
    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    briefing = models.CharField(blank=True, null=True, max_length=255)
    # image_url = models.URLField(blank=True, null=True)
    image_url = models.CharField(blank=True, null=True, max_length=1024)

    price = MoneyField(max_digits=10, decimal_places=2, default_currency='BRL')
    is_sold = models.BooleanField(default=False)

    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Items'
    
    def __str__(self) -> str:
        return self.name