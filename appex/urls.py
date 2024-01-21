from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name='home'),
    path("count", views.counter, name='count'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('details/<str:pk>', views.details, name='details')
]

