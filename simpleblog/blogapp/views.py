from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user # aktueller User als Autor
        return super().form_valid(form)

