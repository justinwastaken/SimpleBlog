from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title.'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What do you wanna talk about.'}), 
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title.'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'What do you wanna talk about.'}), 
        }
