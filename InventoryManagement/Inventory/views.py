from .serializers import UserSerializer

from rest_framework import status


from django.contrib.auth import authenticate


from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny

from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.response import Response



@api_view(['PUT', 'POST', 'GET', 'DELETE'])
def user(request):

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get("password"))
        user.save()
        token = Token.objects.create(user=user)
        data = serializer.data
        data['token'] = token.key
        return Response(data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("email")

    password = request.data.get("password")

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},

                        status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'},

                        status=HTTP_404_NOT_FOUND)

    Token.objects.filter(user=user).delete()

    token, _ = Token.objects.get_or_create(user=user)

    return Response({'token': token.key},

                    status=HTTP_200_OK)



