from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """to manage user profiles"""


    def create_user(self,email,name, password = None):
        """create new user profile"""
        if not email:
            raise valueerror('user must have a vaild email address')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password):
        """create and save a new superuser from given details"""
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for Userprofile. database model users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']


    def get_full_name(self):
        """Retrive full name for user"""
        return self.name

    def get_short_name(self):
        """Retrive short name for user"""
        return self.name

    def __str__(self):
        """Retrive string representation of  user"""
        return self.email
