from django.db import models
# models.py (authentication app)
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    ROLE_CHOICES = [
        ('Accounts', 'Accounts'),
        ('ICT', 'ICT'),
        ('Director', 'Director'),
        ('Director2', 'Director2'),
        ('Manager', 'Manager'),
        ('Marketing', 'Marketing'),
        ('Reception', 'Reception'),
        ('Visionary', 'Visionary'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class LoginBackgroundVideo(models.Model):
    video = models.FileField(upload_to='videos/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Background Video ({self.updated_at})"


class RegisterBackgroundVideo(models.Model):
    video = models.FileField(upload_to='videos/')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Background Video ({self.updated_at})"

