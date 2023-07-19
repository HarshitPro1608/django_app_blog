#from msilib.schema import ListView
from typing import Any, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User 

#from django.http import HttpResponse
from .models import Post
# Create your views here.

# posts = [
#     {
#         'author': 'Harshit',
#         'title': 'Post 1',
#         'content': 'First post',
#         'date_posted':'August 27,2023'
#     },
#     {
#         'author': 'German',
#         'title': 'Post 2',
#         'content': 'Second post',
#         'date_posted':'August 25,2023'
#     }
# ]


def home(request):#function view more coding
    context = {
        'posts': Post.objects.all() #query to get all posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

class PostListView(ListView):#clas based home view,generic view,less coding
    model = Post
    template_name = 'blog/home.html'#will render this(home) template <app>/<model>_<viewtype>.html
    context_object_name = 'posts'#context is given like this
    ordering = ['-date_posted']#ordering posts in latest 
    paginate_by = 5#5 posts per page use /?page=2 for 2nd page and so on
    
    
class UserPostListView(ListView):#clas based home view,generic view,less coding, user specific post view
    model = Post
    template_name = 'blog/home.html'#will render this(home) template <app>/<model>_<viewtype>.html
    context_object_name = 'posts'#context is given like this
    #ordering = ['-date_posted']#ordering posts in latest 
    paginate_by = 5#5 posts per page use /?page=2 for 2nd page and so on
    
    def get_queryset(self):#sorts posts by user posted and matches with author
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
        

class PostDetailView(DetailView):#clas based home view,generic view,less coding,detailed view to toggle to post
    model = Post
    
 #loginrequired mixin is used to redirect user to login page if not logged in and trying to create post   
class PostCreateView(LoginRequiredMixin,CreateView):#class based home view,generic view,less coding,create view to create new post view
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user #make author as current logged in user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):#userpassestet mixin ensures only author can update blog post
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form: BaseModelForm):
        form.instance.author = self.request.user #make author as current logged in user
        return super().form_valid(form) 
    
    def test_func(self):#only allow author to update post
        post = self.get_object()#gets object that we are currently trying to update 
        
        if self.request.user == post.author:#checks weather current user is post author 
            return True
        return False
    
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):#clas based home view,generic view,less coding,detailed view to toggle to post
    model = Post
    success_url = '/'
    
    def test_func(self):#only allow author to delete post
        post = self.get_object()#gets object that we are currently trying to update 
        
        if self.request.user == post.author:#checks weather current user is post author 
            return True
        return False