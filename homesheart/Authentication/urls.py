from django.urls  import path
from.import views 

urlpatterns =[
    path('',views.login, name='login'),
    path('register/',views.register,name='register'),
    path('api/register/',views.register, name='register'),  # The API function
    path('api/login/',views.login, name='login'),  
]