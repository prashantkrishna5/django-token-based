from django.contrib import admin
from django.urls import path, include
from . import views

from userop.views import(LoginView, LogoutView, Home, AddData)


urlpatterns = [
    path('',Home.as_view()),
    path('api/v1/add', AddData.as_view()),
    path('api/v1/auth/login/',LoginView.as_view()),
    path('api/v1/auth/logout/',LogoutView.as_view())

]
