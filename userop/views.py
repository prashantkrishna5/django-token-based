from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from .form import TestQueryForm
from rest_framework import generics
from rest_framework import mixins
from django.http import JsonResponse
from .models import TestQuery
from pprint import pprint
from .serializers import TestQuerySerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request,user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication)

    def post(self, request):
        django_logout(request)
        return Response(status=204)




class Home(APIView):

    def get(self,request):
        testQueryData = TestQuery.objects.all()
        serializer = TestQuerySerializer(testQueryData,many=True)
        return Response(serializer.data)


class AddData(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self,request):
        return Response("Welcome to add")

    def post(self,request):
        t = TestQuery()
        t.State = "state"
        t.ProblemID = 1
        t.ProblemTitle = "title"
        t.MobileNubers = "number"
        t.save()
        return Response("Inserted Sucessfully")

