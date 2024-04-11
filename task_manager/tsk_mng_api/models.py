from django.db import models
from users.models import User


class DailyList(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    comment = models.TextField()
    owner = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"DAY - {self.date} {self.owner.first_name if self.owner else "no owner"}"


class Task(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    complete = models.BooleanField(default=False)
    daily_container = models.ForeignKey(to=DailyList, null=True, blank=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(to=User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"TASK - {self.title} DATE - {self.create_date} COMPLETE - {self.complete}"
