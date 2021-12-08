from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer, UserProfileSerializer
from django.contrib.auth import get_user_model


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    # 1. Client에서 온 데이터를 받아옴
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')

    # 2. 패스워드 일치 여부 확인
    if password != password_confirmation:
        return Response({'ERROR': '비밀번호가 일치하지 않습니다!'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 3. UserSerializer를 통한 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
    # 4. 유효성 검사 / password도 같이 진행
    if serializer.is_valid(raise_exception=True):
        # https://www.django-rest-framework.org/api-guide/serializers/#saving-instances [Saving instances]
        user = serializer.save()

        # 5. 비밀번호 해싱 한 후에 응답
        # https://docs.djangoproject.com/en/3.2/ref/contrib/auth/#django.contrib.auth.models.User.set_password [set_password]
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET'])
def profile(request, username):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=username)

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)