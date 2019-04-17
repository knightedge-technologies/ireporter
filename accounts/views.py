from rest_framework import generics
from . serializers import UserSerializer
from django.contrib.auth.models import User

class SignUp(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer