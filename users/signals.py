from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal to handle additional tasks when a user is created
    """
    if created:
        # Add any additional tasks here when a user is created
        pass

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal to handle additional tasks when a user profile is updated
    """
    # Add any additional tasks here when a user profile is updated
    pass 