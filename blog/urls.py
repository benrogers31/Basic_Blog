from django.urls import path
#. is the current directory 
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    #leave the quotes empty for a home page 
    #when bblog is called and there is nothing after it (hence the '') 
    path('',  PostListView.as_view(), name='blog-home'),
    #<str:username> is the primary key for user and we are throwing it in our routes
    path('user/<str:username>',  UserPostListView.as_view(), name='user-posts'),
    #<int:pk> is the primary key for post and we are throwing it in our routes
    path('post/<int:pk>/',  PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/',  PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',  PostDeleteView.as_view(), name='post-delete'),
    path('post/new/',  PostCreateView.as_view(), name='post-create'),
    #always throw in the trailing slash /
    path('about/', views.about, name ='blog-about'),

]