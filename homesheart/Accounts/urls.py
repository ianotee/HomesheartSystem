from django.urls import path
from .import views


urlpatterns =[
    path('Accounts/',views.Accounts, name='Accounts'),
   
]