# posts/views.py
from rest_framework import generics, viewsets

from .models import Request
from .serializers import RequestSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(['PUT', 'POST', 'GET', 'DELETE'])
def request_detail(request):
   
    if request.method == 'PUT':
        requestId = request.query_params.get('type', None)
        if requestId is not None:
           queryset = Request.objects.get(request_id=requestId) 
        serializer = RequestSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'POST':
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        type = request.query_params.get('type', None)
        if type is not None:
           queryset = Request.objects.filter(type=type) 
           serializer = RequestSerializer(queryset,many=True)
        else:
           queryset = Request.objects.all() 
           serializer = RequestSerializer(queryset,many=True)    
        return Response(serializer.data)

    elif request.method == 'DELETE':
        requestId = request.query_params.get('type', None)
        queryset = Request.objects.get(request_id=requestId)
        queryset.delete()
        return Response(status=status.HTTP_200_OK)                    


@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
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


                