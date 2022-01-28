from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import DIYUsers

# Register your models here.

admin.site.register(DIYUsers, UserAdmin)
