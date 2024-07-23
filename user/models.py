from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **kwargs):
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, password, **kwargs):
        email = ''
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('telegram_chat_id', 1111)
        return self._create_user(email, password, **kwargs)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True,blank = True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    telegram_chat_id = models.BigIntegerField(unique = True,blank=True)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    
    def __str__(self) -> str:
        return self.email


