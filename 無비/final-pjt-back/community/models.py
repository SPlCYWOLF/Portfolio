from django.db import models
from django.conf import settings
from movies.models import Movie

class Review(models.Model):
    RATING = [
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),
    ]
    title = models.CharField(max_length=100)                                                                    # 리뷰글 제목
    rating = models.IntegerField(choices=RATING, default=5)                                                      # 평점
    content = models.TextField()                                                                                # 리뷰글 내용
    created_at = models.DateTimeField(auto_now_add=True)                                                        # 리뷰글 생성
    updated_at = models.DateTimeField(auto_now=True)                                                            # 리뷰글 수정
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_reviews')                    # 영화(1) : 리뷰글(N)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_reviews')   # 유저(1) : 리뷰글(N)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=100)                                                                   # 댓글 내용
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')                 # 리뷰글(1) : 댓글(N)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comments')   # 유저(1) : 댓글(N)

    def __str__(self):
        return self.content