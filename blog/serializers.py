from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Post        # Post 모델 사용
        fields = '__all__'            # 모든 필드 포함
        