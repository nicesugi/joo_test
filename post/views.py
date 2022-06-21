from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from post.serializers import PostSerializer
from user.serializers import UserSerializer

class PostView(APIView):
    # 게시글 조회
    def get(self, request):
        user = request.user
        return Response(UserSerializer(user).data)
    
    
    
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
            print(f'content.id: {content}')

    
    
    # 게시글 수정
    def put(self, request, obj_id):
        content = Post.objects.get(id=obj_id)
        content_serializer = PostSerializer(content, data=request.data, context={"request": request})
        print(f'content_serializer: {(content_serializer)}')
        if content_serializer.is_valid():
            content_serializer.save()
            return Response({"message": "게시글 수정 성공"})
        return Response({"message": "게시글 수정 실패"})
    
    
    
    # 게시글 삭제
    def delete(self, request, obj_id):
        user = request.user
        content = Post.objects.get(id=obj_id)
        if user:
            content.delete()
            return Response({"message": "삭제 성공"})
        return Response({"message": "삭제 실패"})