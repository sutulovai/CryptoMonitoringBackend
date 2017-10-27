from rest_framework.decorators import api_view
from .actions import *

from .serializers import *
from .services.services import *


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_applications_user(request, pk):
    service = init_and_get_applications_user_service()
    return ApplicationsUserViewActions(service=service).process_base_actions(request.method,
                                                                             {"pk": pk, "data": request.data})


@api_view(['GET', 'POST'])
def get_all_or_add_one_app_users(request):
    service = init_and_get_applications_user_service()
    actions = ApplicationsUserViewActions(service=service)
    if request.method == 'GET':
        return actions.get_all()
    elif request.method == 'POST':
        data = {
            'login': request.data.get('login'),
            'password': request.data.get('password'),
        }
        return actions.insert(parameters=data)


def init_and_get_applications_user_service():
    model = ApplicationUser
    serializer = ApplicationUserSerializer
    return ApplicationUserService(model=model, serializer=serializer)


