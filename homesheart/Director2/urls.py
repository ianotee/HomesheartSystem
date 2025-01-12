from django.urls import path 
from .import views

urlpatterns =[
    path('',views.director2, name='director2'),
]