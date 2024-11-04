from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    # def perform_create(self, serializer):
    #     user = serializer.save()
    #     serializer.is_valid(raise_exeption=True)
    #     user.set_password(serializer.validated_data['password'])
    #     user.save()
    #     return user


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            response = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
            return Response(response, status=status.HTTP_200_OK)

        return Response({
            'success': False,
            'message': 'Invalid credentials'
        }, status=status.HTTP_400_BAD_REQUEST)
