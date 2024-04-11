from rest_framework import serializers
from .models import Task, DailyList


class DailyListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=(serializers.CurrentUserDefault))
    class Meta:
        model = DailyList
        fields = ['id', 'create_date', 'date', 'comment', 'owner']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'text', 'create_date', 'deadline', 'daily_container', 'owner']