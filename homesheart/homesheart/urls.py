
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Authentication.views import OTPVerificationView

router = DefaultRouter()




urlpatterns = [
    #Authentication
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/otp/', OTPVerificationView.as_view(), name='otp-verify'),
    #Dashboards
    path('admin/', admin.site.urls),
    path('Accounts/',include('Accounts.urls')),
    path('ICT/', include('ICT.urls')) ,
    path('', include('Authentication.urls')),
    path('Director/', include('Director.urls')),
    path('Director2/', include('Director2.urls')),
    path('Manager/', include('Manager.urls')),
    path('Marketing/', include('Marketing.urls')),
    path('Reception/', include('Reception.urls')),
    path('Visionary/', include('Visionary.urls')),
]



urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


