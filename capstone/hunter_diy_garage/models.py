from django.db import models
from diy_users.models import DIYUsers


class AutoBay(models.Model):

    hours = models.BigIntegerField()


class Reservation(models.Model):

    electricity_used = models.DecimalField(
        default=0.0, max_digits=5, decimal_places=2)
    hours_used = models.DecimalField(
        default=0.0, max_digits=5, decimal_places=2)
    auto_bay_id = models.ForeignKey(
        AutoBay, on_delete=models.SET_NULL, null=True, related_name="reservations")
    diy_user_id = models.ForeignKey(
        DIYUsers, on_delete=models.CASCADE, related_name="reservations")
    date_added = models.DateTimeField(auto_now_add=True)


class Tool(models.Model):

    name = models.CharField(max_length=20)
    cost = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    make = models.CharField(max_length=20)
    checked_out = models.DateTimeField(auto_now_add=True)
    num_times_checked_out = models.SmallIntegerField(default=0)

class NeedleScaler(Tool):

    pass
    
class TorqueWrench(Tool):

    pass

class Welder(Tool):

    pass