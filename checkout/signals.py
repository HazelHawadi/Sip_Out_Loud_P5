from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User  
from .models import Order 

from .models import OrderLineItem

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:  
        UserProfile.objects.create(user=instance)
    else:
        # Check if the user already has a profile before attempting to create one
        if not hasattr(instance, 'userprofile'):
            UserProfile.objects.create(user=instance)