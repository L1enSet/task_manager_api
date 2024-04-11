from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response


class GetUserApi(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
