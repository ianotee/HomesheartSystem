from django.db.models.signals import post_save
from django.dispatch import receiver
from django_otp.plugins.otp_email.models import EmailDevice
from .models import User

@receiver(post_save, sender=User)
def create_otp_device(sender, instance, created, **kwargs):
    if created:
        device = EmailDevice.objects.create(user=instance, name="default")
        device.generate_challenge()
