from django import forms 
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category']
        choices = Category.objects.all().values_list('name', 'name')

        choice_list = []
        for item in choices:
            choice_list.append(item)



        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title.'}),
            'category': forms.Select(attrs={'class': 'form-control'})
            
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title.'}),
            'category': forms.Select(attrs={'class': 'form-control'})
            
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


