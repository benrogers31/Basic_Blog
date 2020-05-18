from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile 

#When a user is saved then we need to send this signal 
#This signal is going to be recieved by this reciver which is for this create profile function 

#arguments are from the post_save signal, instance of user, created checks if user was created
#**kwargs just accepts any additional keyword arguments
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs ):
    if created:
        #we want to create a profile object for this usser
        Profile.objects.create(user = instance )

#this just saves a profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs ):
    instance.profile.save()

##### signals must be imported in the ready funciton of our users apps.py file