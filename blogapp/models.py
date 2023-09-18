from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

STATUS_CHOICES=(
    ("Draft", "Draft"),
    ("Published", "Published")
)


class Blogs(models.Model):
    title=models.CharField(max_length=100)
    slug_field=models.SlugField(max_length=100, unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads')
    shot_description=models.CharField(max_length=500)
    blog_content=models.CharField(max_length=2000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment
