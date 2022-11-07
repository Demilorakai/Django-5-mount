from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import AuthValidateSerializers, RegisValidateSeializers





@api_view(["POST"])
def authorization(request):
    serializer = AuthValidateSerializers(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        try:
            token = Token.objects.get(user=user)
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
        return Response({'key':token.key})
    return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
def registration(request):
   serializer = RegisValidateSeializers(data=request.data)
   serializer.is_valid(raise_exception=True)
   user = User.objects.create_user(**serializer.validated_data)
   return Response(data={
       'id': user.id,
       'username': user.username,
   })