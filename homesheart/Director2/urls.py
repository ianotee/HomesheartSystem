from django.urls import path 
from .import views

urlpatterns =[
    path('',views.Director2, name='Director2'),
]