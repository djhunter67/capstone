from django.urls import path

from . import views

app_name = 'hunter_diy_garage'

urlpatterns = [
    path('', views.index, name='index')
]