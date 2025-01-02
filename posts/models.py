from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    image_filter_choices = [
        ('_1977', '1977'), 
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
        ]
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='../default_post_m65bc6', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_filter = models.CharField(max_length=32, choices=image_filter_choices, default='normal')
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title