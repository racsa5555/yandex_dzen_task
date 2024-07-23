from http import HTTPStatus

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from user.serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegistrationView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)
    

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
