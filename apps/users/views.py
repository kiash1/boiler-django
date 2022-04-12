from rest_framework.generics import (
    ListCreateAPIView,
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from apps.base.base import TokenRegistrationService, TokenMixingService, IrbaseAPIView
from apps.users.serializers import UsersSerializer


class UserListCreateAPIView(IrbaseAPIView, ListCreateAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        return User.objects.all()


class LoginAPIView(GenericAPIView):
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        print("user")

        if user is not None:
            if user:
                login(self.request, user)
                token_service = TokenRegistrationService()
                token_key = token_service.register(user)
                serializer_context = {'request': request}
                serializer = UsersSerializer(user, context=serializer_context)
                data = {
                    'user' : serializer.data,
                    'token' : token_key
                }
                return Response(data)
            else:
                return Response({'error' : 'User is inactive'})

        else:
            return Response({"error" : " Invalid"})


class LogoutAPIView(IrbaseAPIView, TokenMixingService):

    def post(self, request, format=None):
        if request.user.is_anonymous:
            data = {"error" : "no looged in user found"}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)
        else:
            logout(request)
            data = {"sucess" : "Logout Successfully"}
            return Response(status=status.HTTP_204_NO_CONTENT, data=data)
