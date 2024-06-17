from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        email = self.normalize_email(email)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    date_de_naissance = models.DateField(null=True, blank=True)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = CustomUserManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_de_naissance', 'email']
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
