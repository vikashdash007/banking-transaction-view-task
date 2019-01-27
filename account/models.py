from django.db import models
from django.conf import settings

# Create your models here.
User=settings.AUTH_USER_MODEL

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    activated  =models.BooleanField(default=True)
    timestamp  =models.DateTimeField(auto_now=True)
    updated    =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username