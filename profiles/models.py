from django.db import models
# to get signal whenever an event is trigger
# it has 4 options 
# post_save activate event after save 
# pre_delete activate event before  delete
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_att = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = CloudinaryField('image', default='placeholder')

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)