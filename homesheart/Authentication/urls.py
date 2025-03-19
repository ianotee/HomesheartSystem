from django.urls  import path
from.import views 

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns =[
    path('', views.custom_login_page, name='custom_login'),  # Redirect root URL to the login page
    path('login/', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('register_user/', views.register_user, name='register_user'),  # For handling the registration via POST
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path('logout/',views.logout_user, name='logout_user'),
]