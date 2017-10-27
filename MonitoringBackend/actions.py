from rest_framework import status
from rest_framework.response import Response

from .services.services import *


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
        serializer = self.service.serializer(data=parameters)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @abstractmethod
    def get_all(self, ):
        objects = self.service.model.objects.all()
        return Response(self.service.serializer(objects, many=True).data)


class ApplicationsUserViewActions(AbstractViewActions):
    def __init__(self, service):
        super().__init__(service)

    def process_base_actions(self, method_name, parameters):
        return super().process_base_actions(method_name, parameters)

    def insert(self, parameters):
        super().insert(parameters)
