from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f"User ID-{self.id}: {self.first_name} ({self.username}) {self.last_name}"
