from rest_framework import serializers
from .models import Review, Comment

class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    def getUsername(self, objects):
        return objects.user.username

    movie = serializers.CharField(
        source='movie.title',
        read_only=True,
    ),
    
    class Meta:
        model = Review
        fields = '__all__'
        exlcude = ('content', 'rating')
        read_only_fields = ('user',)   # 클라이언트에서 리뷰 리스트 요청시 500 에러 이걸로 해결


class ReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    # userName은 Review 모델에 없음, 따로 정의해서 필드에 담아줌
    def getUsername(self, objects):
        return objects.user.username

    movie = serializers.CharField(
        source='movie.title',
        read_only=True,
    )

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user',)   # 클라이언트에서 리뷰 리스트 요청시 500 에러 이걸로 해결
        

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("getUsername")

    def getUsername(self, objects):
        return objects.user.username

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'review',)