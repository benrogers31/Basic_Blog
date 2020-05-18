from django.shortcuts import render, get_object_or_404
#the . in front of models is because of the current directory 
from .models import Post 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User


#from django.http import HttpResponse



# these are function based views so our URL                         
# patterns are directed to a certain view which are the functions   
# and the functions then handle the logic for the routes and then   
# render the templates                                              

def home(req):
    #when views.home is called it will run this httpresponse 
    #return HttpResponse('<h1> Blog Home </h1>')
    
    context = {
        #this takes all posts from the Post database
        'posts': Post.objects.all()
    }
    
    ##### The render shortcut goes to the templates folder and then goes to the specified html space ie blog/home.html in this case ###
    return render(req, 'blog/home.html', context)



def about(req):
    #when views.about is called it will run this http
    #return HttpResponse('<h1> THIS IS ALL ABOUT BENJAMIN </h1>')
    
    return render(req, 'blog/about.html', {'title' : 'ABOUT PAGE'})


# class based views have alot more built in functionality           
# This handles most of the backend logic for us   
# there are list views, detail views, create views, update views, delete views etc   
# eg we need to list a bunch of posts or videos that would work well for a list view 
# eg when we click on an item in that list we will be looking at content which is more detailed hence detail view   
# We will need to be able to update and delete those views and that would be there own views too 
  
class PostListView(ListView):
    #We need a model to list
    model = Post
    #the default this will look for is <app>/<model>_<viewtype>.html eg blog/post_list.html
    #to change this:
    template_name = 'blog/home.html'
    #this is the name of the thing that will be listed for the html to understand
    context_object_name = 'posts'
    #we want to order how the lists will be viewed
    #if we want to reverse it we would go ['-date_posted']
    ordering = ['-date_posted']
    #shows how many posts to list per page
    paginate_by = 10

#this only lists posts that have been made by the user
class UserPostListView(ListView):

    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    #override
    def get_queryset(self):
        #this gets the user with the specific user name from the URL or it returns as 404 if it cant be found
        user = get_object_or_404(User, username = self.kwargs.get('username') )
        #get_queryset will be overriden so will the ordering feild so we need to order it in here
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    #the default this will look for is <app>/<model>_<viewtype>.html eg blog/post_detail.html



#LoginRequiredMixin basically ensures one is logged to access this view
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    #default for this one is blog/post_form

    def form_valid(self, form):
        #we want to have our current user being the one to write the form 
        form.instance.author = self.request.user
        return super().form_valid(form)

#LoginRequiredMixin basically ensures one is logged to access this view
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    #default for this one is blog/post_form

    def form_valid(self, form):
        #we want to have our current user being the one to write the form 
        form.instance.author = self.request.user
        return super().form_valid(form)

    #this ensures that someone updating a post is the one who wrote it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    #When we delete our posts we need somewhere to go
    success_url = '/'
    #this ensures that someone deleting a post is the one who wrote it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
