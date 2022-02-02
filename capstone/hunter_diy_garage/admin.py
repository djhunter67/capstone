from django.contrib import admin

from .models import (
    AutoBay,
    Tool,
)

# Register your models here.


class AutoBayAdmin(admin.ModelAdmin):

    list_display = ('name', 'hours',)


class ToolAdmin(admin.ModelAdmin):

    list_display = ('name', 'cost', 'make', 'checked_out', 'num_times_checked_out')




admin.site.register(AutoBay, AutoBayAdmin)
admin.site.register(Tool, ToolAdmin)
