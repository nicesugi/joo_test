from rest_framework import serializers
from post.models import Post as PostModel

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostModel
        fields = ["content", "user"]