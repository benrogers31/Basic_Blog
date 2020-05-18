from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    #this ensures a user only has one profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #setting an image feild and making the default deafault.jpg
    #profile_pics will be the directory images get stored in when we upload a profile 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #this is basically how the profile will look as a string 
    def __str__(self):
        return f'{self.user.username} Profile'

    #this is being overridden
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        #getting the image that we saved
        img = Image.open(self.image.path)
        #resizing our images
        #there is a bunch of ways to do this so we can look into it
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)