from django.urls import path

from . import views

app_name = 'hunter_diy_garage'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('blog/', views.blog, name='blog'),
    path('reservation/', views.reservation, name='reservation'),
    path('tools/', views.tools, name='tools'),
    path('bays/', views.bays, name='bays'),
    path('contact/', views.contact, name='contact'),
    path('layout/', views.layout, name='layout'),
    path('cancellation/', views.cancellation, name='cancellation'),
    path('logout/', views.logout, name='logout'),
    path('price/', views.price, name='price'),
    path('rules/', views.rules, name='rules'),
]