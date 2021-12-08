from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Genre(models.Model):
    name = models.TextField()                                                                           # 장르 이름
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_like_genres')            # 유저가 좋아하는 장르

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.TextField()                                                                          # 제목
    original_title = models.TextField()                                                                 # 원래 제목 (영어)
    overview = models.TextField()                                                                       # 줄거리
    poster_path = models.TextField()                                                                    # 포스터
    genres = models.ManyToManyField(Genre)                                                              # 장르
    release_date = models.DateField()                                                                   # 개봉일
    adult = models.BooleanField()                                                                       # 청불
    popularity = models.FloatField(validators=[MinValueValidator(0)])                                   # 인기도
    runtime = models.IntegerField(validators=[MinValueValidator(0)])                                    # 상영시간
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])          # 평점
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])                                 # 투표수
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')            # 유저가 좋아요
    dislike = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dislike_movies')      # 유저가 싫어요

    def __str__(self):
        return self.original_title


