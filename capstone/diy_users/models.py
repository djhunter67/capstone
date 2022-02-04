from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


def upload_path(instance, filename):
    return f"blog/static/img/avatars/{filename}"

# Create your models here.


class DIYUsers(AbstractUser):

    phone_regex = RegexValidator(
        regex=r'\d{10}', message="Phone number must be entered in the format: '+999999999'. 10 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=False)  # validators should be a list
    date_added = models.DateField(auto_now_add=True)
    avatar = models.ImageField(
        upload_to=upload_path, default="../static/img/default_avt.png")

    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    email = models.EmailField(_('email address'), blank=False)

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(DIYUsers, self).save(*args, **kwargs)

