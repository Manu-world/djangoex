from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('update/<str:pk>', views.updateView, name='update'),
    path('<str:pk>/delete', views.deleteView, name='delete')
    
]