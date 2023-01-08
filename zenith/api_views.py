from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .app_exception import AppException
from .services import Services #device_list, login

def Main(request):
    return render(request, 'zenith/main.html')

class Login(APIView):
    def get(self, request):
        id = request.GET.get('id')
        password = request.GET.get('password')
        
        if id is None or password is None:
            raise AppException('input_error', 'input error')

        print('id='+id+' password='+password)

        data = Services.login(request, id, password)
        return Response(data)
    
class List(APIView):
    def get(self, request):
        data = Services.list(request) 
        
        # serializer = PostSerializer(queryset, many=True)
        # return Response(serializer.data)
        return Response(data)
    
class Status(APIView):
    def get(self, request, type, code):
        print('{} {}'.format(type, code))
        
        data = Services.status(request, type, code) 
        
        # serializer = PostSerializer(queryset, many=True)
        # return Response(serializer.data)
        return Response(data)
