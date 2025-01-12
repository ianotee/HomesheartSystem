from django.shortcuts import render
from .models import LoginBackgroundVideo,RegisterBackgroundVideo
from django.shortcuts import render, get_object_or_404
from django_otp.plugins.otp_email.models import EmailDevice
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from django.middleware.csrf import get_token
import requests
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt







@csrf_exempt
def login(request):
    video = LoginBackgroundVideo.objects.last()

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Get CSRF token from the session
        csrf_token = get_token(request)

        # Call the API endpoint to log in using requests
        api_url = request.build_absolute_uri('/api/login/')
        data = {
            'email': email,
            'password': password,
        }
        headers = {'X-CSRFToken': csrf_token}
        response = requests.post(api_url, json=data, headers=headers)

        if response.status_code == 200:  # API returned success
            # Parse the API response (assume it returns user details or a token)
            user_data = response.json()
            
            # Authenticate user locally
            user = authenticate(request, email=email, password=password)
            if user:
                auth_login(request, user)

                # Redirect based on user role
                role_redirects = {
                    "Accounts": "Accounts",
                    "Director": "Director",
                    "Director2": "Director2",
                    "Visionary": "Visionary",
                    "Manager": "Manager",
                    "Reception": "Reception",
                }
                return redirect(role_redirects.get(user.role, 'home'))
            else:
                # If user is not in the local DB, create it or handle error
                messages.error(request, "User authentication failed. Please try again.")
        else:
            # Handle API errors
            messages.error(request, response.json().get("detail", "Invalid email or password."))

    return render(request, 'login.html', {'video': video})







#UserModel = get_user_model()

User = get_user_model()

def register(request):
    video = RegisterBackgroundVideo.objects.last()

    if request.method == "GET":
        # Set the CSRF cookie
        get_token(request)
        return render(request, 'register.html', {'video': video})

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        contact = request.POST.get('contact')

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html', {'video': video})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return render(request, 'register.html', {'video': video})

        try:
            # Create and save the user to the database
            user = User.objects.create_user(username=email, email=email, password=password)

            # If your custom user model includes a `contact` field directly
            user.contact = contact

            # If the `contact` field is part of a related profile model
            # user.profile.contact = contact
            # user.profile.save()

            user.save()

            messages.success(request, "Registration successful. Please log in.")
            return render(request, 'register.html', {'video': video})
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'register.html', {'video': video})

    return render(request, 'register.html', {'video': video})






class OTPVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        device = EmailDevice.objects.filter(user__email=email).first()

        if device and device.verify_token(otp):
            return Response({'message': 'OTP verified successfully!'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
















'''
def login(request):
    video = LoginBackgroundVideo.objects.last()
    return render(request, 'login.html', {'video': video})
'''


'''
def register(request):
    video = RegisterBackgroundVideo.objects.last()
    return render(request, 'register.html', {'video': video})
'''


