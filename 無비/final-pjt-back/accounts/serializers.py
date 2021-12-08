from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# https://www.django-rest-framework.org/api-guide/serializers/#specifying-fields-explicitly [Specifying read only fields]
class UserSerializer(serializers.ModelSerializer):
    
    # https://www.django-rest-framework.org/api-guide/fields/#core-arguments [read_only / write_only]
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        # 11/21 입력 가능한 모든 유저의 입력정보 허용하기 위해 fields 값 수정
        # fields가 이거면 충분한지?! / read-only??


# user profile 확인용
# 11/22 response 해주는 정보들 수정
class UserProfileSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'