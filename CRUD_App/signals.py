from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

from .models import User_Profile

def Profile(sender, instance, created , **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        User_Profile.objects.create(
            user = instance,
            name = instance.username,
        )
        print('profile created!')


post_save.connect(Profile , sender=User)