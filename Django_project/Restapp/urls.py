from django.urls import path
from .views import (TodoListApiView,TodoDetailApiView)
urlpatterns = [
    path("Todo/", TodoListApiView.as_view(),name="TodoListApiView"),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view(),name="TodoDetailApiView"),
]
# from django.urls import include, path
# from rest_framework import routers
# from . import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
