from rest_framework import viewsets, status, authentication, serializers
#, Permissions 
from rest_framework.decorators import action
from rest_framework.response import Response
#from rest_framework.Permissions import AllowAny
from django.contrib.auth.models import PermissionsMixin

#from django.contrib.auth import get_user_model
#from django.core.exceptions import ImproperlyConfigured


from accounts.serializers import UserRegistrationSerializer, UserLoginSerializer
#get_and_authenticate_user


class UserAuthenticationViewset(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path="register")
    def user_registration(self, request):
        user_data = UserRegistrationSerializer(data=request.data)
        if user_data.is_valid():
            user_data.save()
            return Response({"data": user_data.data}, status=status.HTTP_201_CREATED)
        return Response(user_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @action( detail=False, methods=['POST'], url_path="login")
    def user_login(self, request):
        
        #serializer = self.get_serializer(data=request.data)
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.UserLoginSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)

#User = get_user_model()

# class AuthViewSet(viewsets.ViewSet):
#     #Permission_classes = [permissions.AllowAny]
#     # serializer_class = serializer.EmptySerializer
#     serializer_classes = {'login': serializers.UserLoginSerializer}

#     @action( detail=False, methods=['POST'], url_path="login")
#     def user_login(self, request):
        
#         #serializer = self.get_serializer(data=request.data)
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = get_and_authenticate_user(**serializer.validated_data)
#         data = serializers.AuthUserSerializer(user).data
#         return Response(data=data, status=status.HTTP_200_OK)

#     # def get_serializer_class(self):
#     #     if not isinstance(self.serializer_classses, dict):
#     #         raise ImproperlyConfigured("serializer_classes should be in a dict mapping.")
        
#     #     if self.action (self.serializer_classes.keys):
#     #         return super().get_serializer_class()

#     def user_logout(self, request):
#         logout(request)
#         return response.Response("you are logged out")