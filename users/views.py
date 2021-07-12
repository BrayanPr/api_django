from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from users.models import Profile

from users.serializers import UserSerializer

@api_view(['GET'])
def list_client(request):
    if request.method == 'GET':
        users = User.objects.filter(is_staff=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)