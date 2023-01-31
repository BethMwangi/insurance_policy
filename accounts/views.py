from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from .serializers import UserSerializer

from .models import User


class UserListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = (
        'username',
        'email',
        'birth_date',
        'first_name',
    )
    search_fields = ('username', 'email', 'birth_date', 'first_name',)

    ordering_fields = (
        'first_name',
        'created',
    )


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

