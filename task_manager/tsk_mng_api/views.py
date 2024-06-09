from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from datetime import datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class TaskApiView(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    @action(methods=['get'], detail=False, name='to_day_create')
    def new_tsk(self, request):
        queryset = Task.objects.filter(is_complete=False).order_by("-create_date")
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, name='to_day_dead')
    def to_day_dead(self, request):
        dt_now = datetime.now().date()
        queryset = Task.objects.filter(deadline=dt_now, is_complete=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, name='complete')
    def complete(self, request):
        queryset = Task.objects.filter(is_complete=True)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

