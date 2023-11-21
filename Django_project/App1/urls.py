from django.urls import path
from .views import (Landing,login_page,Register_page,LogoutView)

# from fastapi import APIRouter
# from fastapi.responses import HTMLResponse
# router = APIRouter()

urlpatterns = [
    path("",Landing.as_view(),name="Landing"),
    path("login/",login_page.as_view(),name="login_page"),
    path("Register/",Register_page.as_view(),name="Register_page"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
