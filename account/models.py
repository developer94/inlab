from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, null=True)

    present = models.BooleanField(default=False, null=True)

