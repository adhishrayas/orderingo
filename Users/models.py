from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
# Create your models here.


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"),unique=True)
    Profile_picture = models.ImageField("Profile Image",upload_to= "User_profiles/",blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email