from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .app_exception import AppException
from .services import Services

# Create your views here.

class Get(APIView):
    def get(self, request):
        data = Services.proxy_get(request)
        return Response(data)

class Post(APIView):
    def post(self, request):
        data = Services.proxy_post(request)
        return Response(data)
    