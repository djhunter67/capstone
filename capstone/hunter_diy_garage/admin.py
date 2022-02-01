from django.contrib import admin

from .models import (
    AutoBay,
    Tool,
    Reservation,
)

# Register your models here.


class AutoBayAdmin(admin.ModelAdmin):

    list_display = ('hours',)


class ToolAdmin(admin.ModelAdmin):

    list_display = ('name', 'cost', 'make', 'checked_out', 'num_times_checked_out')


class ReservationAdmin(admin.ModelAdmin):

    list_display = ('electricity_used', 'hours_used', 'date_added', 'auto_bay_id', 'diy_user_id')


admin.site.register(AutoBay, AutoBayAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(Reservation, ReservationAdmin)
