from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movies),                                          # 전체 영화 목록
    path('movies/<int:movie_pk>/', views.movie_detail),              # 단일 영화 정보
    path('<int:my_pk>/movies/<movie_title>/like/', views.movie_like),       # 좋아요 기능
    path('<int:my_pk>/movies/<movie_title>/dislike/', views.movie_dislike), # 싫어요 기능
    path('<int:my_pk>/like/', views.my_movie_like),                  # 내가 좋아요 한거
    path('<int:my_pk>/dislike/', views.my_movie_dislike),            # 내가 싫어요 한거
] 