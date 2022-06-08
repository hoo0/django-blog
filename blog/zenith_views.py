from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class DeviceList(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        
        # serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

#json request : data=json.loads(request.body)