from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import Image

@receiver(post_save, sender=User)
def created_image(sender, instance, created, **kwargs):
    if created:
        Image.objects.create(user=instance)

@receiver(post_save, sender=User)
def update_image(sender, instance, **kwargs):
    instance.image.save()