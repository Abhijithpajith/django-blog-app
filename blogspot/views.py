from django.shortcuts import render,redirect,HttpResponse
from .forms import RegForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from blogapp.models import Blogs
from django.db.models import Q


def home(request):
    featured_posts = Blogs.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blogs.objects.filter(is_featured=False, status='Published')

    context={

        'featured_posts':featured_posts,
        'posts':posts,

    }
    return render(request,'home.html',context)


def Register(request):
    if request.method=='POST':
        form=RegForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form=RegForm()
    context={
            'form':form
        }
    return render(request,'register.html',context)


def login(request):
    if request.method == 'POST':
        form= AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user =auth.authenticate(username=username,password=password)
            if user is not None:
               auth.login(request,user)
               return redirect('home')

    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('home')

def search(request):
    keyword=request.GET.get('keyword')
    blogs=Blogs.objects.filter(Q(title__icontains=keyword)|Q(shot_description__icontains=keyword)|Q(blog_content__icontains=keyword),status='Published')
    context={
        'keyword':keyword,
        'blogs':blogs,

    }
    return render(request,'search.html',context)