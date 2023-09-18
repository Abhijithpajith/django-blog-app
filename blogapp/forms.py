from django import forms
from .models import Category,Blogs
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class EditForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=('title','category','image','shot_description','blog_content','is_featured','status')

class EditUser(forms.ModelForm):
    class Meta:
        model=User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups',
                  'user_permissions')