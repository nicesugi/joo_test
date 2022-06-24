from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from post.serializers import PostSerializer
from user.serializers import UserSerializer

class PostView(APIView):
    # 게시글 조회
    def get(self, request):
        # 1 작성자의 게시글만! 조회
        # 1-1 시리얼라이저 사용X
        user = request.user
        print(user)
        posts = Post.objects.filter(user=user).values('user', 'content')
        return Response ({'post': posts})
        
        # 1-2 시리얼라이저 사용O
        # print(request.data)
        # user = request.user
        # return Response(UserSerializer(user).data)
        
        
        # 2 전체 게시글 조회
        # 2-1 시리얼라이저 사용X
        # posts = Post.objects.values('user', 'content') 
        # return Response ({'post': posts})
                # # values() > id, user, content
                # # values('user', 'content') > user, content
    
        # 2-2 시리얼라이저 사용O
        # posts = Post.objects.all()
        # serialized_data = PostSerializer(posts, many=True).data
        # return Response(serialized_data) 
    
    
    
    # 게시글 작성
    def post(self, request):
    # 시리얼라이저 사용X
        # user = request.user
        # content = request.data.get('content', '')
        
        # content, created = Post.objects.get_or_create(
        #     content = content
        #     )
        # if created:
        #     content.user = user
        #     content.save()
        #     print(f'content.id: {content}')
        # return Response({"message":"게시글 작성 성공"})
    
    # 시리얼라이저 사용O
        request.data['user'] = request.user.id
        post_serializer = PostSerializer(data=request.data)
        print(post_serializer)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data)
        return Response(post_serializer.errors)
    
    
    
    # 게시글 수정
    def put(self, request, obj_id):
    # 시리얼라이저 사용X
        # fix_content = Post.objects.get(id=obj_id)
        # fix_content.content = request.data.get('content')
        # fix_content.save()
        
    # 시리얼라이저 사용O
        content = Post.objects.get(id=obj_id)
        content_serializer = PostSerializer(content, data=request.data, context={"request": request})
        print(f'content_serializer: {(content_serializer)}')
        if content_serializer.is_valid():
            content_serializer.save()
            return Response({"message": "게시글 수정 성공"})
        return Response({"message": "게시글 수정 실패"})
    
    
    
    # 게시글 삭제
    def delete(self, request, obj_id):
    # 검증할 것이 없어서 시리얼라이저 사용X
        user = request.user
        content = Post.objects.get(id=obj_id)
        if user:
            content.delete()
            return Response({"message": "삭제 성공"})
        return Response({"message": "삭제 실패"})