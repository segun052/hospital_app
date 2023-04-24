from rest_framework import serializers
#Permissions
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token

#from django.contrib.auth import get_user_model, authenticate

from accounts.models import User, USER_TYPE_CHOICES


class UserRegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        required=True,
        max_length=250,
        min_length=2
    )
    last_name = serializers.CharField(
        required=True,
        max_length=250,
        min_length=2
    )
    username = serializers.CharField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, write_only=True)
    type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        return instance

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, write_only=True)

    # def login_validate(self, attrs);
    #     user = authenticate(email=attrs['email'], password)

# class AuthUserSerializer(serializers.ModelSerializer):
#     auth_token = serializers.SerializerMethodField()

#     class Meta:
#         model = Users
#         fields = ('id', 'email', 'first_name', 'last_name', 'type', 'is_active')
#         read_only_fields = ('id', 'type', 'is_active')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

# class EmptySerializer(serializers.Serializer):
#     pass


#class UserAuthenticate():
    def get_and_authenticate_user(email, password):
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email / password, Please, try again")
        return user