
#here we are gonna handle the logic for our api

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serialiazer import UserSerialiazer

@api_view(['GET'])
def get_users(request):
    users=User.objects.all()
    serializer = UserSerialiazer(users, many=True) 
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):  
    serializer=UserSerialiazer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerialiazer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerialiazer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)