from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='email already in use')
                    ],

    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all(),
                                    message='username already in use')
                    ],
    )
    password = serializers.CharField()

    def create(self, validated_data):
        validate_password(validated_data["password"],
                          user=None,
                          password_validators=None)

        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        return user


    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

