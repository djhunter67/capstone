from django.urls import path

from . import views

app_name = 'hunter_diy_garage'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),    
    path('reservation/', views.reservation, name='reservation'),
    path('tools/', views.tools, name='tools'),
    path('bays/', views.bays, name='bays'),
    path('contact/', views.contact, name='contact'),
    path('layout/', views.layout, name='layout'),
    path('cancellation/', views.cancellation, name='cancellation'),
    path('price/', views.price, name='price'),
    path('rules/', views.rules, name='rules'),
]