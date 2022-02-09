from django.contrib import admin
from .models import DIYUsers

# Register your models here.

class DIYUsersAdmin(admin.ModelAdmin):

    list_display = ('username', 'email', 'first_name', 'phone_number', 'reservation', 'date_added')

admin.site.register(DIYUsers, DIYUsersAdmin)
