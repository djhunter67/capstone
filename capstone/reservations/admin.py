from django.contrib import admin
from .models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('electricity_used', 'hours_used', 'date_reserved', 'auto_bay_id', 'diy_user_id')

admin.site.register(Reservation, ReservationAdmin)
