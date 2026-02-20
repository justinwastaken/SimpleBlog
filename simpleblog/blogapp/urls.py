from django.urls import path
from .views import HomeView, BlogDetailView, AddPostView, UpdatePostView

urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', BlogDetailView.as_view(), name="blog-details"),
    path('add_post', AddPostView.as_view(), name="add_post"),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name="update_post"),
]