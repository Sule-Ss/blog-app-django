from django.contrib import messages
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from blogapp.forms import BlogForm
import users
from .models import Blog, Comment, Favorite
from .forms import CommentForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def blog_list(request):
    blog_list = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blog_list': blog_list})

@login_required
def blog_add(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, "blog created succesfully!")
            return redirect('list')
    context = {
        'form':form
    }
    return render(request, 'blog/blog_add.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    comments = Comment.objects.filter(blog=blog).order_by('-id')
    likeCount = Favorite.objects.filter(blog = blog)
    if request.method == 'POST':
        form = CommentForm(request.POST or None)

        if form.is_valid():
#!save()'i commit=False ile çağırırsanız, o zaman veritabanına henüz kaydedilmemiş bir nesne döndürür. Bir sonraki adımda save ile de kaydedilir.
            comment = form.save(commit=False)
            comment.blog = blog
            comment.user =request.user
            comment.save()

            return redirect('detail', slug=blog.slug)

    else:
        form = CommentForm()
    return render(request, 'blog/blog_detail.html', {'blog':blog, 'form':form, 'comments':comments, 'likeCount':likeCount})

def blog_update(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = BlogForm(instance=blog)
    if request.method == 'POST':
        form =  BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save()
            if 'image' in request.FILES:
                blog.image = request.FILES.get('image')
                blog.save()
            messages.success(request, "blog update succesfully!")
            return redirect('list')
    
    return render(request, 'blog/blog_update.html', {'form': form, 'blog':blog})


def blog_delete(request, slug):
    blog = Blog.objects.get(slug=slug)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog delete succesfully!")
        return redirect('list')
    return render(request, 'blog/blog_delete.html')


def likeView(request, slug):
    blog = Blog.objects.get(slug=slug)
    checkLike = Favorite.objects.filter(user=request.user, blog=blog)
    print(blog)
    if not checkLike:
        likeList= Favorite.objects.create(user=request.user, blog=blog)
        likeList.save()
    else:
        checkLike.delete()
    return redirect('detail', slug=slug)
    # Favorite.objects.get_or_create(user=request.user, blog=blog)
    # context = {
    #     'blog':blog,
    # }
 

