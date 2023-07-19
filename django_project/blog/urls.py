from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('home/',views.home,name='blog-home'),
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),#post/primary key of post to be viewed
    path('post/new/',PostCreateView.as_view(),name='post-create'),#when new post creates it render post_form template
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),#when post update it render post_form template and take primary key to update post
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),#template=post_confirm_delete
    path('about/', views.about,name='blog-about'),
]