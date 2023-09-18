
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .forms import CategoryForm,EditForm,BlogForm,EditUser
from .models import *
from django.contrib.admin.views.decorators import staff_member_required
from django.template.defaultfilters import slugify
# Create your views here.


#add category
@staff_member_required(login_url='login')
def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)

@staff_member_required(login_url='login')
def category(request):

    categyy=Category.objects.all()


    return render(request,'show_category.html',{'categories':categyy})


def edit_cat(request,pk):
    cat=Category.objects.get(pk=pk)
    if request.method == 'POST':
        form=CategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('show_category')
    form=CategoryForm(instance=cat)
    context={
        'form':form,
        'cat':cat
    }
    return render(request,'edi_category.html',context)


def cat_delete(request,id):
    cat=Category.objects.get(id=id)
    cat.delete()
    return redirect('show_category')


#post by category##

def post_by_category(request,category_id):
    posts=Blogs.objects.filter(status='Published',category=category_id)

    category=Category.objects.get(pk=category_id)

    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'post_by_category.html',context)


def blog(request,slug_field):
    single_blog =Blogs.objects.get(slug_field=slug_field,status="Published")
    if request.method=="POST":
        comment=Comment()
        comment.user=request.user
        comment.blogs=single_blog
        comment.comment=request.POST["comment"]
        comment.save()
        return HttpResponseRedirect(request.path_info)

    comments=Comment.objects.filter(blogs=single_blog)
    comments_count=comments.count()

    context={
        'single_blog':single_blog,
        'comments':comments,
        'comments_count': comments_count,
    }
    return render(request,'blogs.html',context)





def dashboard(request):

    if request.user.is_staff:
        blogs_count = Blogs.objects.all().count()
        category = Category.objects.all().count()
        context = {
            'category': category,
            'blogs_count': blogs_count,
        }
        return render(request, 'dashboards.html', context)



    elif request.user.is_authenticated:
      blogs_count = Blogs.objects.filter(author=request.user).count()

      return render(request, 'dashboards.html', {'blogs_count': blogs_count})



def add_post(request):
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            title=form.cleaned_data['title']
            post.slug_field=slugify(title + '-' + str(post.id))
            post.save()
            print(post)
            return redirect('home')
        else:
             print('form is invalid')
             print(form.errors)
    form = BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'add_post.html', context)

def post_view(request):
    if request.user.is_staff:
     posts=Blogs.objects.all()

     return render(request,'posts.html',{'posts':posts})
    elif request.user.is_authenticated:
      posts = Blogs.objects.filter(author=request.user)

      return render(request, 'posts.html', {'posts': posts})


def edit_post(request,pk):
   if request.user.is_staff:
     post=Blogs.objects.get(pk=pk)
     if request.method=="POST":
         form=BlogForm(request.POST,request.FILES,instance=post)
         if form.is_valid():
             post=form.save()
             title=form.cleaned_data['title']
             post.slug_field=slugify(title+'-'+str(post.id))
             post.save()
             return redirect('post_view')
     form=BlogForm(instance=post)
     context={
         'form':form,
         'post':post,
     }

     return render(request,'edit_post.html',context)

   elif request.user.is_authenticated:
       post = Blogs.objects.get(author=request.user,pk=pk)
       if request.method == "POST":
           form = BlogForm(request.POST, request.FILES, instance=post)
           if form.is_valid():
               post = form.save()
               title = form.cleaned_data['title']
               post.slug_field = slugify(title + '-' + str(post.id))
               post.save()
               return redirect('post_view')
       form = BlogForm(instance=post)
       context = {
           'form': form,
           'post': post,
       }

       return render(request, 'edit_post.html', context)

def post_delete(request,pk):
    if request.user.is_staff:
        post=Blogs.objects.get(pk=pk)
        post.delete()
        return redirect('post_view')
    elif request.user.is_authenticated:
        post = Blogs.objects.get(author=request.user,pk=pk)
        post.delete()
        return redirect('post_view')


def users_list(request):
    users=User.objects.all()
    return render(request,'users.html',{'users':users})

def edit_user(request,pk):
    user=User.objects.get(pk=pk)
    if request.method=='POST':
        form=EditUser(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    form=EditUser(instance=user)
    context={
        'form':form,
    }
    return render(request,'edit_user.html',context)

def delete_user(request,pk):
    user=User.objects.get(pk=pk)
    user.delete()
    return redirect('users')