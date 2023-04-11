from django.db import models
from django.apps import apps
import django
from user_app.models import App_User


class Task(models.Model):
    title = models.CharField(max_length=250, unique=True, blank=False, null=False)
    user = models.ForeignKey(App_User, on_delete=models.CASCADE, default=1)