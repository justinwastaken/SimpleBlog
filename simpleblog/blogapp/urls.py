from django.urls import path
from . import views
from .views import HomeView, BlogDetailView

urlpatterns = [
    #path('', views.home, name="home")
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', BlogDetailView.as_view(), name="blog-details")
]