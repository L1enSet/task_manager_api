from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet

class GetUserApi(ModelViewSet):
    queryset = User.objects.get()
    serializer_class = UserSerializer