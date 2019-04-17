from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

