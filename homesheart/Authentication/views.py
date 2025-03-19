
from .models import LoginBackgroundVideo,RegisterBackgroundVideo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, CustomUserSerializer
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django_otp.plugins.otp_email.models import EmailDevice
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from .serializers import UserLoginSerializer, CustomUserSerializer
from .models import LoginBackgroundVideo
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password
import logging
User = get_user_model()

logger = logging.getLogger(__name__)

from django.http import JsonResponse

@csrf_protect
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        logger.info("Received POST request for registration.")

        data = request.data
        email = data.get('email')
        password = data.get('password')
        contact = data.get('contact')
        confirm_password = data.get('confirm-password')

        logger.info(f"Email: {email}, Contact: {contact}, Password: {'*' * len(password)}, Confirm Password: {'*' * len(confirm_password)}")

        if password != confirm_password:
            logger.warning("Passwords do not match.")
            return JsonResponse({'errors': ['Passwords do not match']}, status=400)

        if email and password and contact:
            try:
                user = User.objects.create(
                    username=email,
                    email=email,
                )
                user.set_password(password)
                user.save()
                logger.info(f"User {email} created successfully.")
                return JsonResponse({'message': 'User registered successfully!'}, status=201)
            except Exception as e:
                logger.error(f"Error creating user: {str(e)}")
                return JsonResponse({'errors': [str(e)]}, status=400)

        logger.warning("Some fields are missing.")
        return JsonResponse({'errors': ['All fields are required.']}, status=400)


def custom_login_page(request):
    # You can pass additional context if needed
    return render(request, 'login.html') 

@api_view(["POST"])
def login(request):
    video = LoginBackgroundVideo.objects.last()
    """
    Logs in a user and redirects based on the user's role.
    """
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        # Get the username and password from the validated data
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Authenticate the user manually
        user = authenticate(request, username=username, password=password)

        # Check if authentication is successful
        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect based on the user's role
            role_redirects = {
                'Accounts': '/Accounts/home/',
                'ICT': '/ICT/home/',
                'Director': '/Director/home/',
                'Director2': '/Director2/home/',
                'Manager': '/Manager/home/',
                'Marketing': '/Marketing/home/',
                'Reception': '/Reception/home/',
                'Visionary': '/Visionary/home/',
            }

            # Get the appropriate redirect URL based on the user's role
            redirect_url = role_redirects.get(user.role, '/')  # Default to '/' if role is not found

            return Response({
                "message": "Login successful!", 
                "user": CustomUserSerializer(user).data, 
                "redirect": redirect_url
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "Invalid credentials. Please try again."
            }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "errors": serializer.errors,
        "video": video.url if video else None  # If video exists, return its URL, else None
    }, status=status.HTTP_400_BAD_REQUEST)



@csrf_protect
def register(request):
    return render(request, 'register.html')


@api_view(["POST"])
def logout_user(request):
    """
    Logs out the currently authenticated user.
    """
    logout(request)
    return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)





















