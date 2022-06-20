from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from .models import User
from user.serializers import UserSerializer


class UserView(APIView):

    #사용자조회
    def get(self, request):
        user = request.user
        print(f'request : {user}')
        return Response(UserSerializer(user).data)
    
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        
        user = authenticate(request, username=username, password=password)
        print("로그인 테스트")
        
        if user:
            login(request, user)
            print(f'user: {user}')
            return Response({"message":"로그인 성공"})
            
        return Response({"message":"로그인 실패"})