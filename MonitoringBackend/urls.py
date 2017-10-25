from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^api/v1/app_users/(?P<pk>[0-9]+)$',
        views.get_delete_update_applications_user,
        name='get or delete or update applications user'
    ),
    url(
        r'^api/v1/events/$',
        views.get_all_or_add_one_app_users,
        name='get all applications users or insert one'
    ),
]
