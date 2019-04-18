from rest_framework import status
from django.contrib.auth import login
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth.password_validation import ValidationError
from .serializers import UserSerializer, LoginSerializer
from drf_yasg.utils import swagger_auto_schema


class SignUp(APIView):
    """
    post:
    Register a user.
    """

    serializer_class = UserSerializer
    @swagger_auto_schema(
        operation_description="Create a user account.",
        operation_id="Sign up a user",
        request_body=UserSerializer,
        responses={201: UserSerializer(many=False), 400: "BAD REQUEST"},
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except ValidationError as errors:
                return Response(
                        data={"status": 400,
                              "errors": [errors]
                              },
                        status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                data={
                    "status": status.HTTP_201_CREATED,
                    "data": [
                        {
                            "username": user.username,
                            "email": user.email,
                            "is_admin": user.is_superuser,
                        }
                    ],
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            data={"status": 400, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

class Login(APIView):
    """
    post:
    login a user.
    """

    serializer_class = LoginSerializer
    @swagger_auto_schema(
        operation_description="Login a User",
        operation_id="Login a user",
        request_body=UserSerializer,
        responses={200: UserSerializer(many=False), 401: "Invalid Login"},
    )
    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            data={"Username": serializer.data['username'],
                  "token": serializer.data['token']},
            status=status.HTTP_200_OK

        )