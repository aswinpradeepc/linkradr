from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
import random

class CustomUserManager(BaseUserManager):
    """Manager for CustomUser with email authentication"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)  # ✅ Verification flag
    otp_code = models.CharField(max_length=6, blank=True, null=True)  # ✅ Store OTP
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()  # ✅ Custom manager

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # ✅ Custom related name to avoid clash
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',  # ✅ Custom related name to avoid clash
        blank=True,
    )

    def generate_otp(self):
        """Generate a 6-digit OTP"""
        self.otp_code = str(random.randint(100000, 999999))
        self.save()
