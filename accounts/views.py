from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import SignupSerializer, LoginSerializer

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data # validate()의 리턴값인 token을 받아오기
        return Response({"token": token.key}, status=status.HTTP_200_OK)