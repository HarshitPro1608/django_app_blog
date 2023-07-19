from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
#we want to create profile for each new user automatically

@receiver(post_save,sender=User)#when user creates it sends signal post_save to create_profile reciever function and it takes arguments and then it create profile
def  create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save,sender=User)#save user profile
def  save_profile(sender,instance, **kwargs):
    instance.profile.save()
