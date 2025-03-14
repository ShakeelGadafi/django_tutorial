
#here we are gonna handle the logic for our api

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serialiazer import UserSerialiazer

@api_view(['GET'])
def get_user(request):  
    return Response(UserSerialiazer({'name' : 'shakeel','age': 23}))

 