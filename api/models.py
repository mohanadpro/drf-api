from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

class Software(models.Model):
    title = models.CharField(max_length=50, blank=False)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    external_link = models.URLField(
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )