from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


def upload_path(instance, filename):
    return f"blog/static/img/avatars/{filename}"

# Create your models here.


class DIYUsers(AbstractUser):

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    date_added = models.DateField(auto_now_add=True)
    avatar = models.ImageField(
        upload_to=upload_path, default="../static/img/default_avt.png")

    def __str__(self) -> str:
        return self.username
