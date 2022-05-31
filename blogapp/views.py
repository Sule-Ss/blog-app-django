from django.contrib import messages
from django.shortcuts import redirect, render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from blogapp.forms import BlogForm
from .models import Blog


def home(request):
    return render(request, 'home.html')

def blog_list(request):
    blog_list = Blog.objects.all()
    return render(request, 'blog/blog_list.html', {'blog_list': blog_list})

def blog_add(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            if 'image' in request.FILES:
                blog.image = request.FILES.get('image')
                blog.save()
            messages.success(request, "blog created succesfully!")
            return redirect('list')
    context = {
        'form':form
    }

    return render(request, 'blog/blog_add.html', context)


def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog/blog_detail.html', {'blog':blog})

def blog_update(request, id):
    blog = Blog.objects.get(id=id)
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


def blog_delete(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog delete succesfully!")
        return redirect('list')
    return render(request, 'blog/blog_delete.html')

