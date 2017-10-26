from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .services.services import *


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_applications_user(request, pk):
    model = ApplicationUser
    serializer = ApplicationUserSerializer
    service = ApplicationUserService(model=model, serializer=serializer)
    return ApplicationsUserViewActions(service=service).process_base_actions(request.method,
                                                                             {"pk": pk, "data": request.data})


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


class AbstractViewActions(ABC):
    service = AbstractService

    def __init__(self, service):
        super().__init__()
        self.service = service

    @abstractmethod
    def process_base_actions(self, method_name, parameters):
        serializer = self.service.serializer
        service = self.service
        db_object = service.get_one(pk=parameters.get('pk'))
        if db_object is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if method_name == 'GET':
            return Response(serializer(db_object).data)
        elif method_name == 'DELETE':
            service.delete(db_object)
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif method_name == 'PUT':
            serializer = self.service.serializer(db_object, data=parameters.get('data'))
            if serializer.is_valid():
                service.update(data=parameters.get('data'), pk=parameters.get('pk'))
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @abstractmethod
    def insert(self, parameters):
        serializer = ApplicationUserSerializer(data=parameters)


class ApplicationsUserViewActions(AbstractViewActions):
    def __init__(self, service):
        super().__init__(service)

    def process_base_actions(self, method_name, parameters):
        return super().process_base_actions(method_name, parameters)

    def insert(self, parameters):
        super().insert(parameters)