from django.contrib import admin

# Register your models here.
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):

    list_display = ('title', 'user', 'date_created')
    # list_display_links = ('Blog title', 'Users name')


admin.site.register(BlogPost, BlogPostAdmin)
