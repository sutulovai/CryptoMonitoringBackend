from abc import abstractmethod, ABC

from django.db import models
from rest_framework import serializers


class AbstractService(ABC):
    model = models.Model
    serializer = serializers.ModelSerializer

    def __init__(self, model, serializer):
        super().__init__()
        self.model = model
        self.serializer = serializer

    @abstractmethod
    def get_one(self, pk):
        model = self.model
        try:
            return model.objects.get(pk=pk)
        except model.DoesNotExist:
            return None

    @abstractmethod
    def get_all(self):
        return self.model.objects.all()

    @abstractmethod
    def insert(self, data):
        serializer = self.serializer(self.model, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer.data
        else:
            return None

    @abstractmethod
    def update(self, data, pk):
        model = self.get_one(pk=pk)
        serializer = self.serializer(model, data=data)
        if serializer.is_valid() and model is not None:
            serializer.save()
        else:
            raise model.DoesNotExist

    @abstractmethod
    def delete(self, model):
        model.delete()


class ApplicationUserService(AbstractService):
    def __init__(self, model, serializer):
        super().__init__(model, serializer)

    def delete(self, model):
        super().delete(model)

    def get_all(self):
        return super().get_all()

    def update(self, data, pk):
        return super().update(data, pk)

    def insert(self, data):
        return super().insert(data)

    def get_one(self, pk):
        return super().get_one(pk)