from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt import views
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class TokenObtainPairView(views.TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        access_token_validated = JWTAuthentication().get_validated_token(
            serializer.validated_data["access"]
        )
        user = JWTAuthentication().get_user(access_token_validated)

        return Response(
            {
                "user": UserSerializer(user).data,
                "refresh": serializer.validated_data["refresh"],
                "access": serializer.validated_data["access"],
            },
            status=status.HTTP_200_OK,
        )
