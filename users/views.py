from django.shortcuts import render, redirect
#importing prebuild django code that creates a user
###from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#.forms means from current directory 
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#this import allows us to check if a user is logged in
from django.contrib.auth.decorators import login_required

#have to create a form that will be passed to this view 
#django can deal with alot of the annoying stuff on its own on the backend
def register(req):
    if req.method == 'POST':
        #this creates a form that has the POSTed data 
        form = UserRegisterForm(req.POST) 
        #make sure we get the feilds and data we expect
        if form.is_valid():
            #this saves the user into the database
            form.save()
            #grabs the username, cleaned_data makes sure it is in a clean python type
            username = form.cleaned_data.get('username')
            #this uses an fstring 
            messages.success(req, f'Your account has been created you can now login')
            #this sends the user to the link named blog-home 
            return redirect('login')
    else:
        #this creates a blank form  
        form = UserRegisterForm()
    #then it renders it out into the template
    #in the register html we have a http method that posts the form right back to this route
    return render(req, 'users/register.html', {'form':form})

#this is a decorator: adds functionality to an existing function
@login_required
def profile(req):
    #this is what will be run when we submit our form and possibly pass in new information 
    if req.method == 'POST':
        #here we are basically storing the form models into variables
        #this instance argument allows for there to be default values already there 
        u_form = UserUpdateForm(req.POST, instance= req.user)
        p_form = ProfileUpdateForm(req.POST, req.FILES, instance= req.user.profile)
        ##### req.POST is to put in new data for User, and req.Files is for image data
        #if the forms are valid then we run that bad bo
        if u_form.is_valid() and p_form.is_valid(): 
            u_form.save()
            p_form.save()
             #this uses an fstring 
            messages.success(req, f'Your account has been updated')
            #this sends the user to the link named blog-home 
            return redirect('profile') 

    else: 
        u_form = UserUpdateForm(instance= req.user)
        p_form = ProfileUpdateForm(instance= req.user.profile)
    #we then put these into a dictionary 
    context = {
        'u_form': u_form,
        'p_form': p_form

    }
    #We are now rendering our html passing in the dictionary
    return render(req, 'users/profile.html', context)





##all types of messages###
    # messages.debug
    # messages.info
    # messages.success
    # messages.warning
    # messages.error