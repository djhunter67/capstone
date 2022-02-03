from django.urls import path

from . import views

app_name = 'diy_users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<str:username>', views.profile, name='profile'),
]