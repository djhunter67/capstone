from django.urls import path

from . import views

app_name = 'diy_users'

urlpatterns = [
    path('profile/', views.profile, name='profile')
]