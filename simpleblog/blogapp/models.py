from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255, 
        default="weight lifting", 
        unique=True,
        error_messages={
            "unique": "Diese Kategorie existiert bereits"
        }
    )

    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name.title()
    
    def get_absolute_url(self):
        return reverse('category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    body = CKEditor5Field('Text', config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('home')