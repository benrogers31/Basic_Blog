from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

#this class inherits from Django's prebuilt user creation form
class UserRegisterForm(UserCreationForm):
    #generates an email field default is required=true
    email = forms.EmailField(required = True)

    #Nested namespace for configurations
    class Meta:
        #we specify what we want this model to interact with
        model = User 
        #these are the feilds we want shown on our form and in what order
        fields = ['username', 'email','password1', 'password2']

#model forms allow us to work with a specific database model (Tuple)
#this one will work with our User tuple
class UserUpdateForm(forms.ModelForm):

    email = forms.EmailField(required = True)

    #Nested namespace for configurations
    class Meta:
        #we specify what we want this model to interact with
        model = User 
        #these are the feilds we want shown on our form and in what order
        fields = ['username', 'email']

#This works with the Profile Tuple and updates that
class ProfileUpdateForm(forms.ModelForm):
    class  Meta: 
        model = Profile
        fields = ['image']