import requests
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UsersSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.pop('password2')

        if password != password2:
            raise serializers.ValidationError({"password": "Password not matched"})

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(password)
        user.save()

        url = 'http://127.0.0.1:8001/api/v1/user/create/'
        api_key = "kiash"
        try:
            resp = requests.post(url, json=validated_data,
                                 headers={'Content-Type': 'application/json', 'secrate_key': api_key})
        except Exception as e:
            print(e)

        return user
