from unicodedata import name
from django.db import models
from diy_users.models import DIYUsers

from hunter_diy_garage.models import AutoBay

# Create your models here.


class Reservation(models.Model):

    electricity_used = models.DecimalField(
        default=0.0, max_digits=5, decimal_places=2)
    hours_used = models.DecimalField(
        default=0.0, max_digits=5, decimal_places=2)
    # auto_bay_id = models.ForeignKey(
    # AutoBay, on_delete=models.SET_NULL, null=True, related_name="reservations", to_field="name", unique=True)
    auto_bay_id = models.OneToOneField(
        AutoBay, on_delete=models.SET_NULL, null=True, related_name="reservations")
    diy_user_id = models.ForeignKey(
        DIYUsers, on_delete=models.CASCADE, related_name="reservations")
    date_reserved = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateTimeField()
    time_limit = models.IntegerField(default=0)
