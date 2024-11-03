from django.contrib.auth.models import User
from rest_framework import generics
from django.shortcuts import render

from users.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     serializer.is_valid(raise_exeption=True)
    #     user.set_password(serializer.validated_data['password'])
    #     user.save()
    #     return user
