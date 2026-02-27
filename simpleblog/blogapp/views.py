from django.shortcuts import redirect, render 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import CategoryForm, PostForm, UpdateForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    def get_queryset(self):
        order = self.request.GET.get("order")

        if order == "oldest":
            return Post.objects.order_by("created_at")
        else:
            return Post.objects.order_by("-created_at")
        

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user # aktueller User als Autor
        return super().form_valid(form)
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCategoryView(CreateView):
    model = Category
    fields = ['name']
    template_name = 'add_category.html'
