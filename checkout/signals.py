from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new UserProfile when a new User is created
        UserProfile.objects.create(user=instance)
    else:
        # Ensure the UserProfile exists, then update it
        UserProfile.objects.get_or_create(user=instance)
        instance.userprofile.save()
