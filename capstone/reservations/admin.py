from django.contrib import admin
from .models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):

    list_display = ('reservation_date', 'date_reserved','time_limit', 'auto_bay_id', 'diy_user_id')

admin.site.register(Reservation, ReservationAdmin)
