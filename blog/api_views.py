from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        print(queryset)
        
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

class PostDetail(APIView):
    def get(self, request, pk):
        try:
            queryset = Post.objects.get(pk=pk)
            print(queryset)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(queryset, many=False)
        return Response(serializer.data)

#json request : data=json.loads(request.body)