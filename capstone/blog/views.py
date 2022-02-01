from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from django.urls import reverse

# Create your views here.


def blog(request):
    print("something")
    if request.method == 'GET':

        all_posts = BlogPost.objects.all()
        print(all_posts)
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

    return redirect(reverse("diy_users:profile"))


def search(request):
    """form presented to search for a blog"""

    return render(request, "search.html")


# @login_required
def edit(request, blog_id):
    """form for editing an existing blog"""

    return render(request, "edit.html")

# @login_required
def delete(request, blog_id):
    """form for deleting a user's blog"""

    blog = get_object_or_404(BlogPost, id=blog_id)
    blog.delete()

    return redirect(reverse('diy_users:profile'))
