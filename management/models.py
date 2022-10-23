from email.policy import default
from pyclbr import Class
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Device(models.Model):
    WIN = "WINDOWS"
    LIN = "LINUX"
    
    OS_CHOICES = (
        (WIN, "Windows"),
        (LIN, "Linux")
    )
    name = models.CharField(max_length = 50)
    ipv4 = models.GenericIPAddressField(protocol='IPv4')
    os = models.CharField(max_length=20, choices= OS_CHOICES, default=LIN)
    os_version = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return "{name}, OS: {os}, Version: {os_version}, Ipv4: {ipv4}".format(name=self.name, os=self.os, os_version=self.os_version, ipv4=self.ipv4)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    device_answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return "Device: {device}, Last Pin Response: {device_answered}, Last Time Response: {modified}".format(device=self.device, device_answered=self.device_answered, modified=self.modified)
