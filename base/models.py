from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified= models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, null=True, blank= False)
    last_name = models.CharField(max_length=255, null=True, blank= False)
    
    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return{
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }