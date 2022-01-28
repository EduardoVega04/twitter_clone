from audioop import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
import os
from twitter_clone.settings import BASE_DIR


# Theory here: https://www.youtube.com/watch?v=rEX50LJrFuU
# Don't forget to register the signals in apps.py


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """ Signal triggered after the user is saved into the database. Creates a new profile"""
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


@receiver(post_save, sender=Profile)
def remove_old_user_pics(sender, **kwargs):
    instance = kwargs['instance']
    target_dir = os.path.join(BASE_DIR, 'media', str(instance.user.pk))

    if os.path.exists(target_dir):
        for dirpath, dirnames, filenames in os.walk(target_dir):
            if filenames and len(filenames) > 1:
                list_pics = sorted([os.path.join(dirpath, name)
                                   for name in filenames], key=lambda f: os.path.getmtime(f))
                os.remove(list_pics[0])
