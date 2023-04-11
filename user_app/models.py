from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import apps


# Create your models here.
class App_User(AbstractUser):
    email = models.EmailField(blank = False, null = False, unique = True)
    name = models.CharField(max_length = 255, null = False, blank = False)
    # Tells Django to utilize users email as their username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.name} | {self.email}"
    
apps.register_model(App_User, model=AbstractUser)