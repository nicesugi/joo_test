from rest_framework import serializers
from user.models import User as UserModel
from post.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()
    print(f'post : {posts}')
    
    def get_posts(self, obj):
        print((obj.post_set.all()))

        return [post.content for post in obj.post_set.all()]
    
    class Meta:
        model = UserModel
        fields = ["username","posts"]