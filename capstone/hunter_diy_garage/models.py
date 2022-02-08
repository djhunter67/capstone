from django.db import models


class AutoBay(models.Model):

    name = models.CharField(max_length=10)
    hours = models.BigIntegerField()

    def __str__(self):
        return self.name


class Tool(models.Model):

    CORDLESS = "cordless"
    AIR = "air"
    CORDED = "corded"
    UNDEFINED = "undefined"

    power_type = [
        (CORDLESS, "cordless"),
        (AIR, "air"),
        (CORDED, "corded"),
        (UNDEFINED, "undefined")
    ]

    name = models.CharField(max_length=20)
    cost = models.DecimalField(default=0.0, max_digits=6, decimal_places=2)
    make = models.CharField(max_length=20)
    checked_out = models.DateTimeField(auto_now_add=True)
    num_times_checked_out = models.SmallIntegerField(default=0)
    characteristic = models.CharField(
        max_length=9,
        choices=power_type,
        default=UNDEFINED
    )

    def __str__(self):
        return self.name


# class NeedleScaler(Tool):

#     pass


# class TorqueWrench(Tool):

#     pass


# class Welder(Tool):

#     pass
