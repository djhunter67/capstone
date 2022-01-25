from django.contrib import admin

from .models import (
    AutoBay,
    Tool,
    Reservation,
)

# Register your models here.

admin.site.register(AutoBay)
admin.site.register(Tool)
admin.site.register(Reservation)
