from django.db import models
from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return f"TASK - {self.title} DATE - {self.create_date} COMPLETE - {self.is_complete}"
