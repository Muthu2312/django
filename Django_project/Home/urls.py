from django.urls import path
from .views import Home,ProcessImageView,Result
urlpatterns = [
    path("",Home.as_view(),name="Home"),
    path('process_image/',ProcessImageView.as_view(), name='process_image'),
    path("Result/",Result.as_view(),name="Result"),
]
