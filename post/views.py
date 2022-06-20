from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from post.serializers import PostSerializer


class PostView(APIView):
    # 게시글 조회
    def get(self, request):
        user = request.user
        return Response(PostSerializer(user).data)
    
    # 게시글 작성
    def post(self, request):
        user = request.user
        content = request.data.get('content', '')
        
        content, created = Post.objects.get_or_create(
            content = content
            )
        if created:
            content.user = user
            content.save()
        return Response({"message":"게시글 작성 성공"})
    
    # 게시글 수정
    def put(self, request):
        return Response({"message": "Put 성공"})
    
    # 게시글 삭제
    def delete(self,request):
        return Response({"message": "삭제 성공"})