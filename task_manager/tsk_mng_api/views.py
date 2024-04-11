from django.shortcuts import render
from .models import DailyList, Task
from .serializers import DailyListSerializer, TaskSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class DailyListApiView(ModelViewSet):
    queryset = DailyList.objects.all()
    serializer_class = DailyListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'], name='view_tsk')
    def get_tsk(self, request, pk=None):
        obj = self.get_object()
        queryset = Task.objects.filter(daily_container=obj.id)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskApiView(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

