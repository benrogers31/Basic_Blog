from django.db import models
from django.utils import timezone
#this imports the user table that django already works well with
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


#things that we need to save: Users, posts -> users already have their thing in django so we are gonna work with posts to start

#this is a class post that inherits from class model
#each class is going to be it's own table in the database 
#each attribute will be its own feild in the database
class Post(models.Model):
    
    #A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise. 
    title = models.CharField(max_length = 100)
    #this is such that the text feild has more functionality than a regular text feild  
    content = RichTextUploadingField() 
    #auto_now = changes evertime updated, auto_now_add is only there when it is initialized
    #default = timezone.now takes timezone into account, and only passes the function doesnt execute it 
    date_posted = models.DateTimeField(default = timezone.now)
    # User is foreign key for author, on_delete means when user is deleted then what do we do
    # in this case CASCADE means we also delete the post 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
 

    #this function basically states how the object will be presented as a string 
    def __str__(self):
        return self.title

    #get the url for a specific post and return it as a string 
    #the view will handle the redirect 
    def get_absolute_url(self):
        #gets the full path to post-detail with the primary key in the url
        return reverse('post-detail', kwargs={'pk': self.pk})
