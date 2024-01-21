from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name='home'),
    path("count", views.counter, name='count'),
    path('register', views.register, name='register')
]