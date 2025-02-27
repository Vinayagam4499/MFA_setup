from django.db import models
from django.conf import settings
import pyotp

class TwoFactorAuth(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    otp_secret = models.CharField(max_length=16, blank=True)

    def save(self, *args, **kwargs):
        if not self.otp_secret:
            # Generate a random base32 secret key
            self.otp_secret = pyotp.random_base32()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"2FA for {self.user.username}"
