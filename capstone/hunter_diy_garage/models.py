from django.db import models
from diy_users.models import DIYUsers


class AutoBay(models.Model):

    name = models.CharField(max_length=10)
    hours = models.BigIntegerField()


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
