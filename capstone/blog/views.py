from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from django.urls import reverse

# Create your views here.


def blog(request):
    """All of the created blog posts"""

    if request.method == 'GET':

        all_posts = BlogPost.objects.order_by('-date_created')
        return render(request, "blog.html", {"posts": all_posts})


@login_required
def create(request):
    """form for creating a blog post"""

    if request.method == 'GET':
        return render(request, "create.html")

    form = request.POST

    new_post = BlogPost()
    new_post.user = request.user
    new_post.title = form["title"]
    new_post.body = form["content"]
    new_post.save()

    return redirect(reverse("blog:blog"))


def search(request):
    """form presented to search for a blog"""

    if request.method == 'GET':
        return render(request, "search.html")

    form = request.POST
    print(form)


@login_required
def edit(request, blog_id):
    """form for editing an existing blog"""

    post = get_object_or_404(BlogPost, id=blog_id)

    if request.method == "GET":

        return render(request, "edit.html", {"form": post})

    
    form = request.POST

    post.user = request.user
    post.title = form["title"]
    post.body = form["content"]
    post.save()

    return redirect(reverse("diy_users:profile", args=[request.user]))


@login_required
def delete(request, blog_id):
    """method to delete a user's blog"""

    blog = get_object_or_404(BlogPost, id=blog_id)
    blog.delete()

    return redirect(reverse('diy_users:profile', args=[request.user]))
