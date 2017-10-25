from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_applications_user(request, pk):
    user = ApplicationUser
    try:
        user = ApplicationUser.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        return Response(ApplicationUserSerializer(user).data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ApplicationUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_all_or_add_one_app_users(request):
    if request.method == 'GET':
        users = ApplicationUser.objects.all()
        return Response(ApplicationUserSerializer(users, many=True).data)
    elif request.method == 'POST':
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
        }
        serializer = ApplicationUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
