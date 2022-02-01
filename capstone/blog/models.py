from django.db import models
from diy_users.models import DIYUsers
from django.contrib import admin
# Create your models here.


class BlogPost(models.Model):

    title = models.CharField(max_length=40)

    body = models.TextField(max_length=200)

    user = models.ForeignKey(
        DIYUsers, on_delete=models.CASCADE, related_name='blog_posts')

    public = models.BooleanField(default=False)

    date_created = models.DateTimeField(auto_now_add=True)

    date_edited = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.user

    


