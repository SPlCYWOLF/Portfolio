from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Review, Comment
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from movies.models import Movie


# 전체 리뷰글 조회 (OK)
@api_view(['GET'])
def review_list(request):
    review_list = get_list_or_404(Review)
    serializer = ReviewListSerializer(review_list, many=True)
    return Response(serializer.data)


# 리뷰글 생성 (OK)
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)     # 11/21 수정사항 저장시에 유저가 누군지 알려줌
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'다시 작성하세요~'}, status=status.HTTP_400_BAD_REQUEST)


# 단일 리뷰글 조회/수정/삭제 (OK)
@api_view(['GET','PUT','DELETE'])
def review_detail_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    review_title = review.title     # 리뷰 제목을 남길려고

    # 조회
    if request.method == "GET":
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 수정
    elif request.method == "PUT":
        if review.user == request.user:     # 리뷰 작성자 아니면 컽
            serializer = ReviewSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie)
                return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


    # 삭제
    else:
        if review.user == request.user:     # 리뷰 작성자 아니면 컽
            review.delete()
            return Response({ review_title }, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

# 내 리뷰글 조회 (request, username...)
@api_view(['GET'])
def my_review_list(request, user_id):
    # if request.method == 'GET':
    # review = get_object_or_404(Review, user=user_id)
    # 11/22 수정 사유 & 해결법 아래 링크 참고
    # https://stackoverflow.com/questions/22063748/django-get-returned-more-than-one-topic
    review = Review.objects.filter(user=user_id)    
    serializer = ReviewListSerializer(review, many=True)
    return Response(serializer.data)

# 댓글 생성 (OK)
@api_view(['GET','POST'])
def detail_create_comment(request, review_pk):
    if request.method == 'GET':             # 11/22 댓글 불러오기 로직 생성과 통합
        comment_list = get_list_or_404(Comment)
        serializer = CommentSerializer(comment_list, many=True)
        return Response(serializer.data)
    else:
        review = get_object_or_404(Review, pk=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'다시 작성하세요~'}, status=status.HTTP_400_BAD_REQUEST)


# 댓글 삭제 (틀리진 않은듯)
@api_view(['DELETE'])
def delete_comment(request, review_pk, comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    # comment = review.review_comments.get(pk=comment_pk)

    if request.user==comment.user or request.user.is_superuser:
        comment.delete()
        return Response({'id': comment_pk})
    return Response({'detail': '권한이 없습니다.'})
    # 다르게 메시지를 보여줄 순 없을까?